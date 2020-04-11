from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("home/", views.home, name="home"),
    path("register/",views.register, name="register"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("level1/", views.level_1, name="level_1"),
    path("level2/", views.level_2, name="level_2"),
    path("level3/", views.level_3, name="level_3"),
    path("level4/", views.level_4, name="level_4"),
    path("check_answer/", views.check_answer, name="check_answer")
    # path("solution/",views.solution,name="solution"),
]
