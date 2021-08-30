from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appPrincipal.urls')),
    path('contacto/', include('contacto.urls')),
    path('petshop/', include('petshop.urls')),
    path('adoptar/', include('adoptar.urls')),
    path('turnos/', include('turnos.urls')),
    path('registro/',include('registro.urls')),
    path('carro/',include('carro.urls')),
]
