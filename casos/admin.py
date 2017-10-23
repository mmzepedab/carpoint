from django.contrib import admin

# Register your models here.

from casos.models import (
    Caso
)


class CasoAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "fecha_creado"]

admin.site.register(Caso, CasoAdmin)