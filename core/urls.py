from django.urls import path
from .views import home , carrito,form,info,login,productos

urlpatterns=[
    path('',home, name="home"),
    path('carrito',carrito, name ="carrito"),
    path('form',form, name ="form"),
    path('info',info, name="info"),
    path('login',login, name="login"),
    path('productos',productos, name="productos"),
]