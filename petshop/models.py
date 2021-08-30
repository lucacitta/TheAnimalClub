from django.db import models
from django.utils.html import format_html

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='appPrincipal/static/img')
    disponibilidad=models.BooleanField()
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def foto(self, obj):
        return format_html('<img ser={} />',)


    def __str__(self):
        return self.nombre
