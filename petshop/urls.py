from django.urls import path
from . import views

urlpatterns = [
    path('',views.petshop,name='petshop'),
    path('confirmacionPedido/',views.confirmacionPedido,name='confirmacionPedido'),
]
