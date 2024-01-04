from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Posts, Comment
from .forms import CommentForm, PostForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Posts
    template_name = 'posts/posts_adn_comments.html'
    context_object_name = 'posts'

    # def get_queryset(self):
    #     post_id = self.kwargs['post_id']
    #     return Posts.objects.filter(post_id=post_id)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = Posts.objects.all()
    #     context['posts'] = Posts.objects.get(pk=self.kwargs['post_id'])
    #     return context


class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/posts_adn_comments.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/add_post.html'

    def get_success_url(self):
        return reverse_lazy('books_list')
class CommentListView(ListView):
    model = Comment
    template_name = 'posts/posts_adn_comments.html'
    context_object_name = 'comment'


# def posts_list(request):
#     posts = Posts.objects.all()
#     context = {'posts': posts, 'title': 'Available posts'}
#     return render(request, 'posts/posts_adn_comments.html', context)
#
#
def comments_log(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'posts/comments_list.html', context)


def post_comments(request, post_id=None):

    if post_id:
        comments = Comment.objects.filter(post__pk=post_id)

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

def add_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            comment = comment_form.save()
            return redirect('post_comments', post_id=comment.post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'posts/add_comment.html', {'comment_form': comment_form})
