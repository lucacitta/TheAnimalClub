from django.shortcuts import render, redirect
from django.core.mail import send_mail
from theanimalclub.settings import EMAIL_HOST_USER, EMAIL_ADMIN
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
    print(productos)
    return render(request, 'petshop/petshop.html',{'productos':productos})


def confirmacionPedido(request):
    form=FormularioVenta()
    if request.method=='POST':
        data=request.POST
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        direccion = data.get('direccion')
        telefono = data.get('telefono')
        email = request.user.email

        #email para el cliente
        pedido=''
        total=0
        for key, value in request.session['carro'].items():
            pedido+=f'\nProducto: {value.get("nombre")}, cantidad: {value.get("cantidad")}, subtotal: {value.get("cantidad")*value.get("precio")}'
            total+=int(value.get("cantidad"))*int(value.get("precio"))
        pedido+=f'\nTotal del pedido: {total}'


        send_mail(
            'Confirmacion pedido The Animal Club',
            f'Hola {nombre} {apellido}, tu pedido para {direccion} fue realizado correctamente, nuestro equipo de soporte se contactara contigo dentro de las 48hs habiles.\n'
            f'Detalles del pedido:\n\n{pedido}\n\n'
            'The Animal Club',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False)


        #Email para el administrador

        send_mail(
        f'Tienes un nuevo pedido de {nombre} {apellido}.',
        'holasd',
        EMAIL_HOST_USER,
        [EMAIL_ADMIN],
        fail_silently=False,
        )

        limpiar_carro(request, lugar='confirmacion')
        return redirect('/petshop/confirmacionPedido/?confirmado')
    return render(request,'petshop/confirmacion.html',{'formVenta':form})