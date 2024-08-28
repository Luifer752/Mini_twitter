from django.urls import path
from .views import RegisterView, login_view, logout_view, UsersListView, UserDetailView


urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', UsersListView.as_view(), name="users_list"),
    path('<int:pk>/', UserDetailView.as_view(), name="user_details"),

]
