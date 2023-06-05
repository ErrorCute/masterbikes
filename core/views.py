from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def carrito(request):
    return render(request,'core/carrito.html')

def form(request):
    return render(request,'core/form.html')

def info(request):
    return render(request,'core/info.html')

def login(request):
    return render(request,'core/login.html')

def productos(request):
    return render(request,'core/productos.html')    

def arriendo(request):
    return render(request,'core/arriendo.html')

def servicios(request):
    return render(request,'core/servicios.html')