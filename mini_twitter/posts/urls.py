from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, comments_log, post_comments, add_comment


urlpatterns = [
    path('', PostListView.as_view(), name="posts_list"),
    path('add-post', PostCreateView.as_view(), name='add_post'),
    path('<int:pk>', PostDetailView.as_view(), name="posts_details"),
    path('comments/', comments_log, name="comments_log"),
    path('comments/<str:post_id>', post_comments, name="post_comments"),
    path('add_comment/', add_comment, name='add_comment')
]
