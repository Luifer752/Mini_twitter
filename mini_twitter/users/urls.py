from django.urls import path
from .views import users_list


urlpatterns = [
    path('', users_list, name="users_list"),
    path('<str:username>', users_list, name="filtered_user_list"),

]
