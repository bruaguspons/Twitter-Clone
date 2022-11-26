from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegister
def home(request, *args, **kwargs):
    method = request.method
    if method == 'POST':
        try:
            Post.objects.create(content=request.POST['content'], user=request.user)
        except ValueError as err:
            print(err)
        return redirect('home')

    if method == 'GET':
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

def register(request, *args, **kwargs):
    method = request.method
    context = {
        'error': False,
        'form': UserRegister()
    }
    if method == "POST":
       
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            context['error'] = True
            context['msg'] = 'password is not the same'
            return render(request, 'createUser.html', context)
        else:
            print('------------------------------------')
            form = UserRegister(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('home')
    return render(request, 'createUser.html', context)