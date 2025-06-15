from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Post, Reaction
from rest_framework.exceptions import NotFound
from .serializers import PostSerializer, ReplySerializer
from .serializers import ReactionSerializer
from django.db.models import Count


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user and not request.user.is_staff:
            from rest_framework.response import Response
            from rest_framework import status
            return Response({'detail': 'No tienes permiso para eliminar esto.'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

class ReplyListCreateView(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Post.objects.filter(parent_id=post_id).order_by('created_at')

    def perform_create(self, serializer):
        try:
            parent_post = Post.objects.get(id=self.kwargs['post_id'])
        except Post.DoesNotExist:
            raise NotFound("Post principal no encontrado.")
        serializer.save(author=self.request.user, parent=parent_post)


class ReactToPostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        emoji = request.data.get("emoji")
        if emoji not in dict(Reaction.EMOJI_CHOICES):
            return Response({"error": "Emoji no permitido."}, status=status.HTTP_400_BAD_REQUEST)

        reaction, created = Reaction.objects.get_or_create(
            user=request.user, post_id=post_id, emoji=emoji
        )
        if not created:
            return Response({"detail": "Ya reaccionaste con ese emoji."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Reacción registrada."}, status=status.HTTP_201_CREATED)


class ReactionSummaryView(APIView):
    def get(self, request, post_id):
        summary = (
            Reaction.objects
            .filter(post_id=post_id)
            .values('emoji')
            .annotate(count=Count('emoji'))
            .order_by('-count')
        )
        return Response(summary)