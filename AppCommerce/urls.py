from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('bienvenida', views.login, name="bienvenida"),
    path('billetera/<int:usuarioid>', views.billetera, name="billetera")
]