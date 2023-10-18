from django.shortcuts import render
from django.http import HttpResponse

from .models import Users


def index(request):
    user = Users.objects.all()
    context = {'user': user}
    return HttpResponse(user)


def test(request):
    print(dir(request))
    return HttpResponse("<h1>USERS TITLE</h1>")
