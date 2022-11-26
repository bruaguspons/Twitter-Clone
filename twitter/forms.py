from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'first_name',
            'username',
            'password1',
            'password2'
        ]
