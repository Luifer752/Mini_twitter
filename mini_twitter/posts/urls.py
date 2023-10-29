from django.urls import path
from .views import posts_list, comments_log, filtered_posts, post_comments, add_post


urlpatterns = [
    path('', posts_list, name="posts_list"),
    path('add-post', add_post, name='add_post'),
    path('<str:user_or_id>', filtered_posts, name="filtered_posts"),
    path('comments/', comments_log, name="comments_log"),
    path('comments/<str:post_id>', post_comments, name="post_comments"),

]