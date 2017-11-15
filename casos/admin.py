# -*- coding: 850 -*-
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django import forms
from django.contrib.auth.models import User

# Register your models here.

from casos.models import (
    Caso,
    Aseguradora,
    Avance,
    UsuarioAseguradora
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


class AvanceInline(admin.StackedInline):
    model = Avance
    readonly_fields = ['fecha_creado']
    extra = 0
    show_change_link = False

class CasoAdmin(admin.ModelAdmin):
    form = CasoAdminForm
    fields = (
        ('descripcion', 'estado_caso_id'),
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
    inlines = [
        AvanceInline,
    ]


class AseguradoraAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    search_fields = ['nombre']

class AvanceAdmin(admin.ModelAdmin):
    model = Avance

class UsuarioAseguradoraAdmin(admin.ModelAdmin):
    model = UsuarioAseguradora
    search_fields = ['aseguradora__nombre', 'usuario__username']

admin.site.register(Avance, AvanceAdmin)
admin.site.register(Caso, CasoAdmin)
admin.site.register(Aseguradora, AseguradoraAdmin)
admin.site.register(UsuarioAseguradora, UsuarioAseguradoraAdmin)
