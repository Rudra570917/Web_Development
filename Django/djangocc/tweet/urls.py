from django.shortcuts import render,redirect
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path("",views.index,name="index")
]