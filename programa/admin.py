from django.contrib import admin

from programa.models import Manutencao, ManutencaoArquivo, ManutencaoLog, Situacao


class ManutencaoLogInline(admin.TabularInline):
    model = ManutencaoLog


class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ['edificio', 'data', 'procedimento', 'frequencia']
    ordering = ['edificio', 'data']
    inlines = [ManutencaoLogInline]

    @admin.display()
    def procedimento(self, obj):
        return obj.edificio_procedimento.procedimento

    @admin.display()
    def frequencia(self, obj):
        return obj.edificio_procedimento.procedimento.periodo

admin.site.register(Manutencao, ManutencaoAdmin)
admin.site.register(ManutencaoLog)
admin.site.register(ManutencaoArquivo)
admin.site.register(Situacao)
