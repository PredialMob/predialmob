from django.contrib import admin

from programa.models import Manutencao, ManutencaoArquivo, ManutencaoLog, ProgramaMixin, Situacao

admin.site.register(Manutencao)
admin.site.register(ManutencaoLog)
admin.site.register(ManutencaoArquivo)
admin.site.register(Situacao)
