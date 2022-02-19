
from django.urls import path, include
from . import views


urlpatterns = [
    path('wholesaler', views.wholesalerboard, name="wholesalerboard"),
]