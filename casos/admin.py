from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

# Register your models here.

from casos.models import (
    Caso,
    Aseguradora
)



class CasoAdminForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = '__all__'
        widgets = {
          'asegurado':forms.RadioSelect,
          'transmision': forms.RadioSelect,
          'personal': forms.RadioSelect,
        }

class CasoAdmin(admin.ModelAdmin):
    form = CasoAdminForm
    fields = (
        'descripcion',
        ('cliente', 'aseguradora'),
        ('marca', 'modelo', 'anio'),
        ('color', 'placa', 'tipo'),
        ('kilometros', 'vin'),
        ('asegurado', 'transmision', 'personal'),
        'observaciones',
    )
    list_display = ["id","descripcion", "fecha_creado"]
    search_fields = ['id', "cliente__username"]
    raw_id_fields = ('cliente',)


class AseguradoraAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    search_fields = ['nombre']

admin.site.register(Caso, CasoAdmin)
admin.site.register(Aseguradora, AseguradoraAdmin)