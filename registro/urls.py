from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registrarse/',views.register, name='registrarse'),
    path('ingresar/', LoginView.as_view(template_name='registro/login.html'), name='ingresar'),
    path('salir/', LogoutView.as_view(template_name='registro/logout.html'), name='salir'),
]
