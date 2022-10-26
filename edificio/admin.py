from django.contrib import admin

from edificio.models import Edificio, EdificioSistemas


class EdificioSistemaInline(admin.TabularInline):
    model = EdificioSistemas

class EdificioAdmin(admin.ModelAdmin):
    inlines = [EdificioSistemaInline]


admin.site.register(Edificio, EdificioAdmin)
