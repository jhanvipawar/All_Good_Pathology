from django.contrib import admin
from django.urls import path,include  
from home import views
from . import views


urlpatterns = [
    path("", views.firstpage, name='home'),
    path("cart", views.cart , name='cart'),
    path("login", views.login , name='login'),
    path("register", views.register , name='register')



]