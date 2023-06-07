from django.shortcuts import render
from .models import Pedido,Usuario

def Pedidos(request):
    pedidos= Pedido.objects.all()
    data = {
        'pedidos':pedidos
    }

    return render(request,'core/Pedidos.html',data)  

def carrito(request):
    return render(request,'core/carrito.html')



def form(request):
    return render(request,'core/form.html')

def info(request):
    return render(request,'core/info.html')

def login(request):
    Usuarios= Usuario.objects.all()
    data = {
        'usuarios':Usuarios
    }
    return render(request,'core/login.html',data)


def productos(request):
    return render(request,'core/productos.html')  


def arriendo(request):
    return render(request,'core/arriendo.html')  

def servicios(request):
    return render(request,'core/servicios.html')  



def base(request):
    return render(request,'core/base.html')  

def vistaArriendo(request):
    return render(request,'core/vistaArriendo.html')



