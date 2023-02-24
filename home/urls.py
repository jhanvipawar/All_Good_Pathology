from django.contrib import admin
from django.urls import path,include 
from home import views
from . import views
from .views import logout



urlpatterns = [
    path("", views.firstpage, name='home'),
    path("cart", views.cart , name='cart'),
    path("login", views.login_p , name='login'),
    path("logout", views.logout_p, name='logout'),
    path("register", views.register , name='register'),
    #path("homepage", views.homepage , name='login'),
    path("profile", views.profile , name='profile'),
    path("forgetpassword", views.forgertpassword , name='forgertpassword'),
    path("about", views.about , name='about'),
    path("feedback", views.feedback , name='feedback'),
    path("register_a", views.register_a , name='register_a'),
    path("login_a", views.login_a , name='login'),

    #path("test_page",views.test_page , name='test_page'),
    path("testpage/<int:id>",views.testpage,name='testpage'),
    path("packagepage/<int:id>",views.packagepage,name='packagepage')


]