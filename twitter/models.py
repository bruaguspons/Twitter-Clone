from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Your Bio', max_length=255)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    Created_At = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering= ['-Created_At']

    def __str__(self):
        return self.content