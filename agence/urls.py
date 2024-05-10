from django.urls import path
from . import views
from .views import *
from .views import hotel_reservation, register_view, login_view


urlpatterns = [
    path('',home, name="home"),
    path('login',login, name="login"),
    path('register',register,name="register"),
    path('gallerie',gallerie,name="gallerie"),
    path('propos',propos, name="propos"),
    path('hotel-reservation/', hotel_reservation, name='hotel_reservation'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
