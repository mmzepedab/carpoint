# -*- coding: 850 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core import serializers

# Create your models here.

class Aseguradora (models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):  # __unicode__ on Python
        return self.nombre

class UsuarioAseguradora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios')
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.CASCADE, related_name='aseguradoras')
    class Meta:
        unique_together = ('aseguradora', 'usuario')
    def __str__(self):  # __unicode__ on Python
        return "Usuario: " + str(self.usuario) + " -> Aseguradora: " + str(self.aseguradora)

class Caso(models.Model):
    ESTADO_CASO = (
		(1, 'Iniciado'),
		(2, 'En Proceso'),
		(3, 'Completado'),
    )
    SI_NO_CHOICES = (
        (1, "Si"),
        (0, "No"),
    )
    MECANICO_AUTOMATICO_CHOICES = (
        (1, "Mecanico"),
        (0, "Automatico"),
    )
    descripcion = models.CharField(max_length=200)
    estado_caso_id = models.IntegerField(default=1, choices=ESTADO_CASO)
    observaciones = models.CharField(max_length=200)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='casos')
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.CASCADE, related_name='casos', null=True, blank=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    #Vehiculo
    marca = models.CharField(max_length=200, null=True)
    modelo = models.CharField(max_length=200, null=True)
    anio = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    placa = models.CharField(max_length=200, null=True)
    tipo = models.CharField(max_length=200, null=True)
    kilometros = models.CharField(max_length=200, null=True)
    vin = models.CharField(max_length=200, null=True)
    asegurado = models.IntegerField(choices=SI_NO_CHOICES, default=1)
    transmision = models.IntegerField(choices=MECANICO_AUTOMATICO_CHOICES, default=1)
    personal = models.IntegerField(choices=SI_NO_CHOICES, default=1)
    def __str__(self):              # __unicode__ on Python
   		return "Caso Id# " + str(self.id)

class Avance(models.Model):
    fecha_creado = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    imagen_1 = models.ImageField(upload_to='images/', null=True, blank=True)
    imagen_2 = models.ImageField(upload_to='images/', null=True, blank=True)
    imagen_3 = models.ImageField(upload_to='images/', null=True, blank=True)
    imagen_4 = models.ImageField(upload_to='images/', null=True, blank=True)
    imagen_5 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.descripcion
