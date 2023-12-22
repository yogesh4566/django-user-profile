from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('about',views.about, name="about"),
    path('service',views.service, name="about"),
    path('contact',views.contact, name="contacts"),
]
