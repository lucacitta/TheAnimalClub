from django.shortcuts import render
from datetime import date
from django.core.mail import send_mail
from theanimalclub.settings import EMAIL_HOST_USER, EMAIL_ADMIN

def turnos(request):
    fechaActual=date.today()
    if request.method=='POST':
        data=request.POST
        nombre=data.get('nombre')
        email=data.get('email')
        fecha=data.get('fecha')
        consulta=data.get('consulta')
        #ESPACIO PARA VERIFICACION DE LA FECHA



        #ESPACIO PARA VERIFICACION DE LA FECHA

        #Email para el cliente
        send_mail(
            'Confirmacion de cita The Animal Club',
            f'Hola {nombre}, tu cita para la fecha {fecha} a sido agendada correctamente, por favor, en caso '
            'de ausencia, avisar con 48 horas de anticipacion, muchas gracias por confiar en nosotros.\nThe animal Club.',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        #Email para el administrador
        send_mail(
            f'Nueva cita para {fecha}',
            f'En la fecha {fechaActual}, {nombre} realizo una cita para {fecha} con la siguiente consulta:\n{consulta}',
            EMAIL_HOST_USER,
            [EMAIL_ADMIN],
            fail_silently=False
        ) 
    return render(request,'turnos/turnos.html',{})
