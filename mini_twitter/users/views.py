from django.shortcuts import render
from django.http import HttpResponse

from .models import Users


def index(request):
    users = Users.objects.all()
    context = {'users': users, 'title': 'Users list'}
    return render(request, 'users/users_list.html', context)


def test(request):
    print(dir(request))
    return HttpResponse("<h1>USERS TITLE</h1>")
