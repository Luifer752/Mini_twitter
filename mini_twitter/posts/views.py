from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts, Comment


def index(request, username=None):
    if username:
        posts = Posts.objects.filter(user__username=username)
    else:
        posts = Posts.objects.all()
    context = {'posts': posts, 'title': 'Available posts'}
    return render(request, 'posts/posts_adn_comments.html', context)


def comments_log(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'posts/comments_list.html', context)


# def posts_by_user(request, user):
#     posts = Posts.objects.all()
#     context = {'posts': posts, 'title': 'Available posts'}
#     for i in posts:
#         if user == i.user:
#             return render(request, 'posts/comments_list.html', context)

