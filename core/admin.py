from django.contrib import admin
from . models import Cliente,Pedido,SolicitudArriendo,Bicicleta

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','numeroTelefono','correo','fecha_nacimiento']
    search_fields=['rut','nombre']


class PedidosAdmin(admin.ModelAdmin):
    list_display=['nro_orden','id_detalle','cod_producto','fecha_compra','fecha_despacho','fecha_entrega','cliente']    
    search_fields=['nro_orden']
    list_filter=['fecha_compra']


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Pedido, PedidosAdmin)
admin.site.register(SolicitudArriendo)
admin.site.register(Bicicleta)