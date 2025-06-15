from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]

class Reaction(models.Model):
    EMOJI_CHOICES = [
        ('❤️', 'Corazón'),
        ('😮', 'Sorpresa'),
        ('💡', 'Idea'),
        ('😂', 'Risa'),
        ('😢', 'Tristeza'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    emoji = models.CharField(max_length=2, choices=EMOJI_CHOICES)
    reacted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'emoji')