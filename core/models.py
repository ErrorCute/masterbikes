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



class Bicicleta(models.Model):
    id_bicileta= models.CharField(primary_key=True,max_length=20)
    nombre= models.CharField(max_length=100)
    modelo=models.CharField(max_length=30)
    disponible= models.BooleanField()

    def __str__(self):
        return self.modelo



class SolicitudArriendo(models.Model):

    id_arriendo=models.AutoField(primary_key=True)
    bicicleta=models.ForeignKey(Bicicleta,on_delete=CASCADE)
    fecha_arriendo=models.DateField(blank=False,null=False)
    cantidad=models.IntegerField()
    opciones = (
        (True, 'Disponible'),
        (False, 'No disponible'),
    )
    estado=models.BooleanField(choices=opciones)
    
    def __str__(self):
        return str(self.id_arriendo)
   
    def get_estado_display(self):
        if self.estado:
            return 'Disponible'
        else:
            return 'No disponible'


class Producto (models.Model):
    
    nombre=models.CharField(max_length=64)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


