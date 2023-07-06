from django.urls import path
from .views import agregar_producto, base,carrito, eliminar_producto,form,info, limpiar_carrito,login,productos,arriendo, restar_producto,servicios,vistaArriendo,Pedidos,eliminar_solicitud,mod_arrien

urlpatterns=[
  
    path('',base,name="base"),
    path('carrito',carrito, name ="carrito"),
    path('form',form, name ="form"),
    path('info',info, name="info"),
    path('login',login, name="login"),
    path('productos',productos, name="productos"),
    path('arriendo',arriendo, name="arriendo"),
    path('servicios',servicios, name="servicios"),
    path('vistaArriendo',vistaArriendo,name="vistaArriendo"),
    path('pedidos',Pedidos, name="pedidos"),
    path('eliminar_solicitud/<id>/',eliminar_solicitud, name="eliminar_solicitud"),
    
    path('mod_arrien/<id>/',mod_arrien, name="mod_arrien"),
    

    
    path('carrito',carrito, name ="carrito"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    



]