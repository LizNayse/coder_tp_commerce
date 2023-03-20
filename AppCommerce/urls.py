from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('usuario', views.login, name="usuario"),
    path('billetera', views.billetera, name="billetera")
]