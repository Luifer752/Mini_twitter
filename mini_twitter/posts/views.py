from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts, Comment


def index(request):
    posts = Posts.objects.all()
    comments = Comment.objects.all()
    context = {'posts': posts, 'comments': comments, 'title': 'Available posts'}
    return render(request, 'posts/posts_adn_comments.html', context)


def test(request):
    print(dir(request))
    return HttpResponse("<h1>POSTS TITLE</h1>")
