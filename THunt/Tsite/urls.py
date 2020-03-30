from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("home/", views.home, name="home"),
    path("register/",views.register, name="register"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("level1/", views.level_1, name="level_1")
    # path("solution/",views.solution,name="solution"),
]
