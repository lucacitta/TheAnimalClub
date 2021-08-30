from django.urls import path
from . import views

urlpatterns = [
    path('',views.adoptar, name='adoptar'),
    path('formulario/',views.adoptar_form, name='adoptar_form'),
]
