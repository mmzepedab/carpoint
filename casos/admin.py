from django.contrib import admin

# Register your models here.

from casos.models import (
    Caso
)


class CasoAdmin(admin.ModelAdmin):
    list_display = ["id","descripcion", "fecha_creado"]
    search_fields = ['id']

admin.site.register(Caso, CasoAdmin)