from django import forms
from users.models import Users


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
