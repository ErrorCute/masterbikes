from django.shortcuts import render,redirect
from .models import Pedido,SolicitudArriendo,Bicicleta
from django.contrib.auth.decorators import login_required,permission_required
from .forms import UsuarioUserForm,Nuevasolicitud,Modificarestado
from django.contrib.auth import authenticate,login

@login_required
def Pedidos(request):
    pedidos= Pedido.objects.all()
    data = {
        'pedidos':pedidos
    }

    return render(request,'core/Pedidos.html',data)  


def carrito(request):
    return render(request,'core/carrito.html')



def form(request):
    data = {
        'form': UsuarioUserForm()
    }
    if request.method == 'POST':
        formulario = UsuarioUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
           
            return redirect('base')
        
    
    return render(request,'registration/form.html',data)


def info(request):
    return render(request,'core/info.html')




def productos(request):
    return render(request,'core/productos.html')



def servicios(request):
    return render(request,'core/servicios.html')  



def base(request):
    return render(request,'core/base.html')  


def vistaArriendo(request):





    return render(request,'core/vistaArriendo.html')



















@login_required
def arriendo(request):
    solicituds= SolicitudArriendo.objects.all()
    data = {
        
        'solicituds':solicituds ,
        'form': Nuevasolicitud()
    }
    if request.method == 'POST':
        formulario= Nuevasolicitud(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mesaje']= "guardado correctamente"
    

    return render(request,'core/arriendo.html',data)  


 

def eliminar_solicitud(request, id):
    solicitud = SolicitudArriendo.objects.get(id_arriendo=id)
    solicitud.delete()

    return redirect(to="arriendo")


def mod_arrien(request, id):
    solicituds = SolicitudArriendo.objects.get(id_arriendo=id)
    data = {
            'form': Modificarestado()
            }
    if request.method == 'POST':
        formulario = Modificarestado(data=request.POST, instance=solicituds)
        if formulario.is_valid():
            formulario.save()
            data['mesaje'] = "modificado correctamente"
            data['form']= formulario

            return redirect(to="arriendo")
            


    return render(request,'core/mod_arrien.html',data)