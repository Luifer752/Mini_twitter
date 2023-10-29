from django import forms
from django.forms.widgets import HiddenInput
from users.models import Users
from posts.models import Posts, Comment


class PostForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())
    title = forms.CharField(max_length=128)
    content = forms.CharField(widget=forms.Textarea)

    created_at = forms.DateTimeField(widget=HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].widget = forms.HiddenInput()


class CommentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())
    post = forms.ModelChoiceField(queryset=Posts.objects.all())
    content = forms.CharField(max_length=256)

    created_at = forms.DateTimeField(widget=HiddenInput)
