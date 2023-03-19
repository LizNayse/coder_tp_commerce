from django.contrib import admin
from . models import *

admin.site.register(Usuario)
admin.site.register(Billetera)
admin.site.register(Producto)
admin.site.register(Publicacion)
admin.site.register(Factura)

# Register your models here.