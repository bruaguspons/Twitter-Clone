from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from django.utils import timezone

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Your Bio', max_length=255)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=False, max_length=140)
    Created_At = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-Created_At']

    def __str__(self):
        return self.content
    
    def clean(self):
        if self.content == "":
            raise ValidationError("content can not be empty!")
        if len(self.content) > 140:
            raise ValidationError("content must not have more than 140 characters")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Post, self).save(*args, **kwargs)