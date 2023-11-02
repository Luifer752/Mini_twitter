from django.shortcuts import render
from django.http import HttpResponse

from .models import Users


def users_list(request, username=None):

    if username:
        users = Users.objects.filter(username=username)
    else:
        users = Users.objects.all()

    context = {'users': users, 'title': 'Users list'}
    return render(request, 'users/users_list.html', context)





