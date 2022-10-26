from django.db import models
from django.utils.translation import gettext as _

from core.models import PmModelEdificio, DescricaoMixin


class ProgramaMixin(models.Model):
    situacao = models.ForeignKey(to='Situacao', to_field='sid', on_delete=models.DO_NOTHING)
    indice = models.PositiveIntegerField()
    data = models.DateField()

    class Meta:
        abstract = True


class Manutencao(ProgramaMixin, PmModelEdificio):
    sistema_edificio = models.ForeignKey(to='edificio.EdificioSistemas', to_field='sid', on_delete=models.CASCADE)
    procedimento = models.ForeignKey(to='sistema.Procedimento', on_delete=models.CASCADE)

    def __str__(self):
        return self.procedimento.descricao + ' ' + str(self.indice)

    class Meta:
        verbose_name = _('manutenção')
        verbose_name_plural = _('manutenções')


class ManutencaoLog(ProgramaMixin, PmModelEdificio):
    usuario = models.ForeignKey(to='core.Usuario', to_field='sid', on_delete=models.DO_NOTHING)
    manutencao = models.ForeignKey(to='Manutencao', to_field='sid', on_delete=models.CASCADE, verbose_name=_('manutenção'))
    indice = models.PositiveIntegerField()
    notas = models.TextField()

    class Meta:
        verbose_name = _('log de manutenção')
        verbose_name_plural = _('logs de manutenção')


class ManutencaoArquivo(DescricaoMixin, PmModelEdificio):
    manutencao = models.ForeignKey(to='ManutencaoLog', to_field='sid', on_delete=models.CASCADE)
    arquivo = models.FileField()

    class Meta:
        verbose_name = _('Arquivo de manutenção')
        verbose_name_plural = _('Arquivos de manutenção')


class Situacao(DescricaoMixin, PmModelEdificio):
    aberto = models.BooleanField(default=True)
    cor = models.CharField(max_length=9, default='#888888')

    class Meta:
        verbose_name = _('situação')
        verbose_name_plural = _('situações')
