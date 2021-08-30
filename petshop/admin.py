from django.contrib import admin
from .models import Producto
from django.utils.html import format_html
# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'precio',
        'foto'
    )
    search_fields = ['nombre',]
    readonly_fields=('updated',)

    def foto(self, obj):

        return format_html('<img scr={}/>', obj.imagen.url)

admin.site.register(Producto, ProductosAdmin)