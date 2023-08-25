from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import date
from django.db import models


# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=40, default='Santiago')
    pais = models.CharField(max_length=40, default='Chile')

    def __str__(self) -> str:
        return f'{self.nombre}{self.ciudad}{self.pais}'
    
class Director_general(models.Model):
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40, default='laboratorio')
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
        primary_key=True,
        )  

    def __str__(self) -> str:
        return f'{self.nombre}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        )
    f_fabricacion = models.DateField(
        validators = [MinValueValidator(limit_value=date(2015, 1, 1))]
        )
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.nombre}{self.laboratorio}{self.f_fabricacion}{self.p_costo}{self.p_venta}'
    
class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.visit_count} visits"