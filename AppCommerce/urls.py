from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('usuario', views.login, name="usuario"),
    path('billetera', views.billetera, name="billetera"),
    path('publicar', views.publicar_producto, name="publicar"),
    path('producto_publicado/<int:producto_id>', views.producto_publicado, name="producto_publicado")
]