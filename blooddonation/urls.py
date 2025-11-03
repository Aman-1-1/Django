from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_now", views.logindoner_view, name="login"),
    path("signup_now", views.signupdoner_view, name="signup"), 
    path("home_page", views.home, name="home"), 
    path("logout_done", views.logout_view, name="logout"), 
    path("find_doner", views.finddoner, name="finddoner"), 
]