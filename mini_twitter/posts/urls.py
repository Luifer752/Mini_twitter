from django.urls import path
from .views import posts_list, comments_log, filtered_posts


urlpatterns = [
    path('', posts_list, name="posts_list"),
    path('<str:user_or_id>', filtered_posts, name="filtered_posts"),
    path('comments/', comments_log, name="comments_log"),

]