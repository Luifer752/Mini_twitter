from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)