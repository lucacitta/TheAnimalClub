from django.urls import path
from . import views

urlpatterns = [
    path('',views.turnos, name='turnos'),
]
