from django.contrib import admin

from sistema.models import Periodo, Procedimento, ProcedimentoReferencias, Referencia, Responsavel, Sistema


class ProcedimentoInline(admin.TabularInline):
    model = Procedimento


class SistemaAdmin(admin.ModelAdmin):
    inlines = [ProcedimentoInline]


class ReferenciaInline(admin.TabularInline):
    model = ProcedimentoReferencias
    extra = 1


class ProcedimentoAdmin(admin.ModelAdmin):
    inlines = [ReferenciaInline]
    raw_id_fields = ['sistema']


admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Procedimento, ProcedimentoAdmin)
admin.site.register(Responsavel)
admin.site.register(Referencia)
admin.site.register(Periodo)
