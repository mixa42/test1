from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    #path('reg/<str:login>/<str:passw>/', views.register_new, name="register_new"),
    path('', views.index, name='index'),
]


