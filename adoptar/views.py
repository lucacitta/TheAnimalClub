from django.shortcuts import render, redirect
from django.core.mail import send_mail
from theanimalclub.settings import EMAIL_HOST_USER, EMAIL_ADMIN

def adoptar(request):
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
        return redirect('/adoptar/?valido')
    return render(request,'adoptar/adoptar.html',{})

def adoptar_form(request):
    if request.method=='POST':
        data=request.POST
        email=data.get('email')
        sexo=data.get('sexo')
        edad=data.get('edad')
        info=data.get('info')
        # Email para el cliente
        send_mail(
            'Confirmacion solicitud de adopción',
            f'Saludos, tu solicitud se registro correctamente, nos estaremos comunicando a la brevedad, de antemano, gracias por querer darle un hogar a uno de nuestros michis\n'
            'Informacion de la solicitud: \n\n'
            f'Sexo preferido: {sexo}\n'
            f'Edad preferida: {edad}\n'
            f'Mensaje de solicitud: {info}\n',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False
            )
        # Email para el administrador
        send_mail(
            'Nueva solicitud de adopcion',
            f'Se registro una nueva solicitud con los siguientes datos: \n\n'
            f'Email del solicitante: {email}\n'
            f'Sexo preferido: {sexo}\n'
            f'Edad preferida: {edad}\n'
            f'Mensaje de solicitud: {info}\n',
            EMAIL_HOST_USER,
            [EMAIL_ADMIN],
            fail_silently=False
            )
    return render(request,'adoptar/adoptar_form.html',{})
