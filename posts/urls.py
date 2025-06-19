from django.urls import path
from .views import PostListCreateView, PostDetailView, ReplyListCreateView, ReactToPostView, ReactionSummaryView, \
    ActivePostsTodayView, TopPostsView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/replies/', ReplyListCreateView.as_view(), name='post-replies'),
    path('posts/<int:post_id>/react/', ReactToPostView.as_view(), name='react-to-post'),
    path('posts/<int:post_id>/reactions/', ReactionSummaryView.as_view(), name='reaction-summary'),
    path('stats/active/', ActivePostsTodayView.as_view(), name='active-posts-today'),
    path('stats/top/', TopPostsView.as_view(), name='top-posts'),
]