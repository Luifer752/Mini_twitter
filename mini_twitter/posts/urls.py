from django.urls import path
from .views import posts_list, comments_log


urlpatterns = [
    path('', posts_list, name="posts_list"),
    path('<str:username>', posts_list, name="filtered_posts_list"),
    path('comments/', comments_log, name="comments_log"),

]