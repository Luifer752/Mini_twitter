from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='users/profile_img', null=True, blank=True)

    def __str__(self):
        return f'User {self.username},' \
               f'email address is: {self.email}'

