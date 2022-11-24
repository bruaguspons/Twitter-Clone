from django.urls import path
from .views import home
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
]
