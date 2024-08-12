from django.db import models
from custom_auth.models import CustomUser


class Users(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # username = models.CharField(max_length=128)
    # email = models.CharField(max_length=128, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='static/user_img', null=True, blank=True)
    bio = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

