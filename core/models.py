from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Cliente(models.Model):
    rut= models.CharField(primary_key=True,max_length=11)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    numeroTelefono=models.IntegerField()
    correo= models.EmailField(max_length=50)
    fecha_nacimiento= models.DateField(blank=False, null=False)

    def __str__(self) :
        return self.nombre


class Pedido(models.Model):
    nro_orden = models.CharField(primary_key=True,max_length=11)
    id_detalle = models.CharField(max_length=150)
    cod_producto = models.CharField(max_length=16)
    fecha_compra = models.DateField(blank=False, null=False)
    fecha_despacho = models.DateField(blank=False, null=False)
    fecha_entrega = models.DateField(blank=False, null=False)
    cliente = models.ForeignKey(Cliente,on_delete=CASCADE)
   
    def __str__(self):
        return self.nro_orden
    


class Usuario(models.Model):
    usuario= models.CharField(primary_key=True,max_length=11)
    clave =models.CharField(max_length=100)
    rut =models.ForeignKey(Cliente,on_delete=CASCADE)

