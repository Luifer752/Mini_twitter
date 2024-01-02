from django.db import models
from users.models import Users


class Posts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    post_picture = models.ImageField(upload_to='static/post_img', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user}" \
               f" {self.post}" \
               f" {self.content}"
