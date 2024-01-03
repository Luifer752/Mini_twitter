from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Users


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class FilteredUsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Users.objects.filter(pk=pk)


# def users_list(request, username=None):
#
#     if username:
#         users = Users.objects.filter(username=username)
#     else:
#         users = Users.objects.all()
#
#     context = {'users': users, 'title': 'Users list'}
#     return render(request, 'users/users_list.html', context)





