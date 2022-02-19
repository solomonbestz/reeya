from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signupchoice', views.signupchoice, name='signupchoice'),
    path('signupwholesaler', views.signupwholsaler, name='signupwholesaler'),
    path('signupreseller', views.signupreseller, name='signupreseller'),
    path('loginchoice', views.loginchoice, name='loginchoice'),
    path('loginwholesaler', views.loginwholesaler, name='loginwholesaler'),
    path('loginreseller', views.loginreseller, name='loginreseller'),
    path('signout', views.signout, name='signout'),

]
