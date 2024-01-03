from django.urls import path
from .views import UsersListView, FilteredUsersListView


urlpatterns = [
    path('', UsersListView.as_view(), name="users_list"),
    path('<int:pk>', FilteredUsersListView.as_view(), name="filtered_user_list"),

]
