from django.contrib import admin

from edificio.models import Edificio, EdificioSistemas, EdificioProcedimento


class EdificioSistemaInline(admin.TabularInline):
    model = EdificioSistemas
    extra = 1
    raw_id_fields = ['sistema']


class EdificioProcedimentoInline(admin.TabularInline):
    model = EdificioProcedimento
    readonly_fields = ['detalhes', 'sistema', 'procedimento']
    fields = ['ativo', 'procedimento', 'detalhes', 'sistema']
    can_delete = False
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    @admin.display()
    def detalhes(self, obj):
        return obj.procedimento.detalhes


class EdificioAdmin(admin.ModelAdmin):
    inlines = [EdificioSistemaInline, EdificioProcedimentoInline]


admin.site.register(Edificio, EdificioAdmin)
