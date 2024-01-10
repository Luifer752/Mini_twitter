from django import forms
from django.forms import ModelForm
from users.models import Users
from posts.models import Posts, Comment
from django.utils import timezone


# class PostForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=Users.objects.all())
#     title = forms.CharField(max_length=128, label='My title')
#     content = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['user', 'title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']

