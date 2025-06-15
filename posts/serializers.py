from rest_framework import serializers
from .models import Post, Reaction


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'parent']
        read_only_fields = ['id', 'author', 'created_at', 'parent']

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'user', 'post', 'emoji', 'reacted_at']
        read_only_fields = ['id', 'user', 'post', 'reacted_at']