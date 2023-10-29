from django import forms
from django.forms.widgets import HiddenInput
from users.models import Users
from posts.models import Posts, Comment
from django.utils import timezone


class PostForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())
    title = forms.CharField(max_length=128, label='My title')
    content = forms.CharField(widget=forms.Textarea)

    created_at = forms.DateTimeField(initial=timezone.now)



class CommentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())
    post = forms.ModelChoiceField(queryset=Posts.objects.all())
    content = forms.CharField(max_length=256)

    created_at = forms.DateTimeField(initial=timezone.now)
