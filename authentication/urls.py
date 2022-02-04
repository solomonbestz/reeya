from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signupchoice', views.signupchoice, name='signupchoice'),
    path('signupwholesaler', views.signupwholsaler, name='signupwholesaler'),
    path('signupreseller', views.signupreseller, name='signupreseller'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

]
