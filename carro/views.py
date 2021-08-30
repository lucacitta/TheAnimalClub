from django.shortcuts import redirect
from .carro import Carro
from petshop.models import Producto

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('petshop')

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('petshop')

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('petshop')

def limpiar_carro(request, lugar='petshop'):
    carro=Carro(request)
    carro.limpiar_carro()
    if lugar=='petshop':
        return redirect('petshop')
    else:
        return redirect('/petshop/confirmacionPedido/?valido')


