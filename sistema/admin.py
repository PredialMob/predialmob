from django.contrib import admin

from sistema.models import Periodo, Procedimento, ProcedimentoReferencias, Referencia, Responsavel, Sistema

admin.site.register(Sistema)
admin.site.register(Procedimento)
admin.site.register(Responsavel)
admin.site.register(Referencia)
admin.site.register(ProcedimentoReferencias)
admin.site.register(Periodo)
