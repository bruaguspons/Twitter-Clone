from django.shortcuts import render

def home(request, *args, **kwargs):
    return render(request, 'home.html', {
        'user': {
            'img':False,
            'des': "you know who i am hjhjhhjhhjjjj",
            'followers': 10,
            'following': 20
        }
    })
