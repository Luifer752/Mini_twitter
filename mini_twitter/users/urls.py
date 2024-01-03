from django.urls import path
from .views import UsersListView, UserDetailView


urlpatterns = [
    path('', UsersListView.as_view(), name="users_list"),
    path('<int:pk>', UserDetailView.as_view(), name="user_details"),

]
