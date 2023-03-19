from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre=models.CharField(max_length=256)
    contrasenia=models.CharField(max_length=8)
    email=models.EmailField()

    def __str__(self) -> str:
        return self.nombre

class Billetera(models.Model):

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)    
    efectivo=models.IntegerField()

class Producto(models.Model):

    nombre=models.CharField(max_length=256)
    descripcion=models.CharField(max_length=600)

class Publicacion(models.Model):

    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio=models.IntegerField()
    stock=models.IntegerField()

class Factura(models.Model):

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo=models.CharField(max_length=1)
    precio_unitario=models.IntegerField()
    cantidad=models.IntegerField()
    fecha=models.DateField()
