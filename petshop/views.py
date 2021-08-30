from django.shortcuts import render, redirect
from django.core.mail import send_mail
from theanimalclub.settings import EMAIL_HOST_USER
from .models import Producto
from carro.views import limpiar_carro
from .forms import FormularioVenta

def petshop(request):
    productos=Producto.objects.all()
    if request.method=='POST':
        data=request.POST
        if data.get('emailRegistro'):
            email=data.get('emailRegistro')
            send_mail(
                'Bienvenido a nuestro newsletter!!',
                'Bienvenido, nos alegra mucho que hayas decidido sumarte y recibir las ultimas noticias sobre The Animal Club\n'
                'Apartir de ahora recibiras todas las actualizaciones sobre nuestro sitio web, muchas gracias.\n'
                'The Animal Club',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            return redirect('/petshop/?valido')
        else:
            print('no entro')
    return render(request, 'petshop/petshop.html',{'productos':productos})


def confirmacionPedido(request):
    form=FormularioVenta()
    if request.method=='POST':
        form=request.POST
        limpiar_carro(request, lugar='confirmacion')
        return redirect('/petshop/confirmacionPedido/?confirmado')
    return render(request,'petshop/confirmacion.html',{'formVenta':form})
