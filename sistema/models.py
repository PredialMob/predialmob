from datetime import date

from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils.translation import gettext as _

from core.models import PmModel, DescricaoMixin
from programa.models import Manutencao


class Sistema(PmModel):
    nome = models.CharField(max_length=120)

    def get_manutencoes_queryset(self):
        return Manutencao.objects.filter(sistema_edificio__sistema=self)

    def get_manutencoes_abertas(self):
        return self.get_manutencoes_queryset().filter(situacao__aberto=True).count()

    def get_manutencoes_total(self):
        return self.get_manutencoes_queryset().count()

    def __str__(self):
        return self.nome


class Procedimento(DescricaoMixin, PmModel):
    sistema = models.ForeignKey(to='sistema.Sistema', on_delete=models.CASCADE)
    subsistema = models.CharField(max_length=120, null=True, blank=True, verbose_name=_('sub-sistema'))
    periodo = models.ForeignKey(to='sistema.Periodo', on_delete=models.CASCADE, verbose_name=_('período'))
    responsaveis = models.ManyToManyField(to='sistema.Responsavel', verbose_name=_('responsáveis'))
    referencias = models.ManyToManyField(
        to='sistema.Referencia', through='sistema.ProcedimentoReferencias', verbose_name=_('referências')
    )
    detalhes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao


class Responsavel(DescricaoMixin, PmModel):
    descricao_length = 120

    class Meta:
        verbose_name = _('responsável')
        verbose_name_plural = _('responsáveis')


class Referencia(DescricaoMixin, PmModel):
    descricao_length = 120
    anexo = models.FileField(upload_to='media/referencia/', null=True, blank=True)

    class Meta:
        verbose_name = _('referência')


class ProcedimentoReferencias(PmModel):
    procedimento = models.ForeignKey(to='sistema.Procedimento', on_delete=models.CASCADE)
    referencia = models.ForeignKey(to='sistema.Referencia', on_delete=models.CASCADE)
    pagina = models.CharField(max_length=20, null=True, blank=True)
    artigo = models.CharField(max_length=20, null=True, blank=True)
    paragrafo = models.CharField(max_length=20, null=True, blank=True)
    detalhes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'sistema_procedimento_referencias'
        verbose_name = _('procedimento referência')
        verbose_name_plural = _('procedimentos referências')


class Periodo(PmModel):
    periodo = models.IntegerField(verbose_name=_('período'))
    tipo = models.CharField(
        max_length=1, choices=[('Z', _('dias')), ('S', _('semanas')), ('M', _('meses')), ('A', _('anos'))]
    )

    def get_proxima_data(self, data):
        if self.tipo == 'Z':
            return data + relativedelta(days=self.periodo)
        if self.tipo == 'S':
            return data + relativedelta(weeks=self.periodo)
        if self.tipo == 'M':
            return data + relativedelta(months=self.periodo)
        if self.tipo == 'A':
            return data + relativedelta(years=self.periodo)
        return data

    def get_datas(self, inicio, final):
        datas = []
        data = self.get_proxima_data(inicio)
        while data <= final:
            datas.append(data)
            data = self.get_proxima_data(data)
        return datas

    def __str__(self):
        field_object = self._meta.get_field('tipo')
        if self.periodo != 1:
            return str(self.periodo) + ' ' + dict(field_object.choices)[self.tipo]
        elif self.tipo == 'M':
            return str(self.periodo) + ' ' + _('mês')
        return str(self.periodo) + ' ' + dict(field_object.choices)[self.tipo][:-1]

    class Meta:
        verbose_name = _('período')
