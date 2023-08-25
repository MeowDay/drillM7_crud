from django.contrib import admin
from .models import Laboratorio, Director_general, Producto
# Register your models here.

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre')
@admin.register(Director_general)
class DirectorAdmin(admin.ModelAdmin):
    list_display=('nombre', 'laboratorio')
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')