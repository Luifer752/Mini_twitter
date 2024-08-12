from django.urls import path
from .views import UsersListView, UserDetailView, edit_profile


urlpatterns = [
    path('', UsersListView.as_view(), name="users_list"),
    path('<int:pk>/', UserDetailView.as_view(), name="user_details"),
    path('<int:user_id>/edit-profile/', edit_profile, name='edit_profile')

]
