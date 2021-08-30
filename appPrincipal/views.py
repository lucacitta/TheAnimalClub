from django.shortcuts import render, redirect
from theanimalclub.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def index(request):
    if request.method=='POST':
        data=request.POST
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
        return redirect('/?valido')
    return render (request,'appPrincipal/index.html',{})

def servicios(request):
    if request.method=='POST':
        data=request.POST
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
        return redirect('/?valido')
    return render (request,'appPrincipal/servicios.html',{})
