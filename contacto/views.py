from django.shortcuts import render, redirect
from django.core.mail import send_mail
from theanimalclub.settings import EMAIL_HOST_USER, EMAIL_ADMIN

def contacto(request):
    if request.method=="POST":
        data=request.POST
        nombre=data.get('nombre')
        email=data.get('email')
        sexo=data.get('sexo')
        consulta=data.get('consulta')
        subcribirse=data.get('subs')
        if subcribirse == 'on':
            subs='El usuario se suscribio al newsletter'
        else:
            subs=''
                                    #EMAIL PARA EL ADMINISTRADOR
        send_mail(
            f'{nombre} a realizado una consulta en The Animal Club',
            f'Datos:\n\n'
            f'{nombre} con email {email} y sexo {sexo} realizó la siguiente consulta:\n\n'
            f'{consulta}\n\n'
            f'{subs}',
            EMAIL_HOST_USER,
            [EMAIL_ADMIN],
            fail_silently=False,
        )
                                    #EMAIL PARA EL CLIENTE
        if subcribirse == 'on':
            subs='\nGracias por subscribrse al newsletter, apartir de ahora recibira nuestras ultimas noticias.\n'
        else:
            subs=''
        send_mail(
            f'Gracias por tu consulta en The Animal Club',
            f'Hola {nombre}, recibimos correctamente tu consulta, te respoderemos en las proximas 48 horas habiles.\n'
            f'{subs}'
            f'Muchas gracias por comunicarte, The Animal Club.',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return redirect('/contacto/?valido')
    return render(request,'contacto/contacto.html',{})
