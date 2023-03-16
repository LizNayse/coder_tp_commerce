from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre=models.CharField(max_length=256)
    contrasenia=models.CharField(max_length=8)
    email=models.EmailField()