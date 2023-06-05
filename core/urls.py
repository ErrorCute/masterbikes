from django.urls import path
from .views import home , carrito,form,info,login,productos,arriendo,servicios

urlpatterns=[
    path('',home, name="home"),
    path('carrito',carrito, name ="carrito"),
    path('form',form, name ="form"),
    path('info',info, name="info"),
    path('login',login, name="login"),
    path('productos',productos, name="productos"),
    path('arriendo',arriendo,name="arriendo"),
    path('servicios',servicios,name="servicios"),
]