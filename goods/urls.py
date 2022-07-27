from django.contrib import admin
from django.urls import path
from goods import views

urlpatterns = [
    path('categories', views.categories.as_view()),
]
