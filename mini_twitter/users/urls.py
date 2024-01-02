from django.urls import path
from .views import UsersListView



urlpatterns = [
    path('', UsersListView.as_view(), name="users_list"),
    path('<str:username>', UsersListView.as_view(), name="filtered_user_list"),

]
