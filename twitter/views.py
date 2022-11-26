from django.shortcuts import render
from .models import Post
def home(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'user': {
            'img':False,
            'des': "you know who i am hjhjhhjhhjjjj",
            'followers': 10,
            'following': 20
        }
    })
