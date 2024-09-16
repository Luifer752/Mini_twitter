from django.urls import path
from .views import UserUpdateView


urlpatterns = [
    path('users/edit-profile/', UserUpdateView.as_view(), name='edit_profile')
]
