from django.urls import path
from .views import mostrar, agregar, editar, edit_labs, eliminar, inicio_test

urlpatterns = [
    path('', mostrar, name='mostrar'),
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>/', editar, name='editar'),   
    path('edit_labs/', edit_labs, name='edit_labs'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
    path('inicio_test', inicio_test, name='inicio')
]