from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

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