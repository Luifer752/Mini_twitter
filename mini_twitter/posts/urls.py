from django.urls import path
from .views import index, comments_log


urlpatterns = [
    path('', index, name="index"),
    path('<str:username>', index, name="filtered_index"),
    path('comments/', comments_log, name="comments_log"),

]