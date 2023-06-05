from django.urls import path
from .views import base,home,carrito,form,info,login,productos

urlpatterns=[
  
    path('',base,name="base"),
    path('home',home, name="home"),
    path('carrito',carrito, name ="carrito"),
    path('form',form, name ="form"),
    path('info',info, name="info"),
    path('login',login, name="login"),
    path('productos',productos, name="productos"),

]