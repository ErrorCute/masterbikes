from django.urls import path
from .views import base,carrito,form,info,login,productos,arriendo,servicios,vistaArriendo,Pedidos,eliminar_solicitud

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
    
    



]