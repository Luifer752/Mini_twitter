from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts, Comment


def posts_list(request):
    posts = Posts.objects.all()

    context = {'posts': posts, 'title': 'Available posts'}
    return render(request, 'posts/posts_adn_comments.html', context)


def comments_log(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'posts/comments_list.html', context)


def filtered_posts(request, user_or_id=None):

    if user_or_id.isdigit():
        posts = Posts.objects.filter(pk=user_or_id)
    elif not user_or_id.isdigit():
        user_or_id = user_or_id.capitalize()
        posts = Posts.objects.filter(user__username=user_or_id)

    context = {'posts': posts, 'title': 'Available posts'}
    return render(request, 'posts/posts_adn_comments.html', context)
