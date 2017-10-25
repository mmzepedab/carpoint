from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Caso(models.Model):
    ESTADO_CASO = (
		(1, 'Iniciado'),
		(2, 'En Proceso'),
		(3, 'Completado'),
    )
    descripcion = models.CharField(max_length=200)
    estado_caso_id = models.IntegerField(default=1, choices=ESTADO_CASO)
    observaciones = models.CharField(max_length=200)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='casos', default=1)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    def __str__(self):              # __unicode__ on Python
   		return "Caso Id# " + str(self.id)