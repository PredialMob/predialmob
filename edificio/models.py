import uuid

from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext as _

from config.models import ConfigEdificio
from core.models import PmModel, PmModelEdificio
from programa.models import Manutencao
from sistema.models import Procedimento


class Edificio(PmModel):
    sid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=120)
    sistemas = models.ManyToManyField(to='sistema.Sistema', through='EdificioSistemas')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('edifício')


class EdificioSistemas(PmModelEdificio):
    sistema = models.ForeignKey(to='sistema.Sistema', on_delete=models.CASCADE)
    inicio = models.DateField()
    final = models.DateField()

    def __str__(self):
        return self.edificio.nome + ' - ' + self.sistema.nome

    class Meta:
        db_table = 'edificio_edificio_sistemas'
        verbose_name = _('sistema do edifício')
        verbose_name_plural = _('sistemas do edifício')
        unique_together = ['sistema', 'edificio']

@receiver(models.signals.post_save, sender=EdificioSistemas)
def post_save_edificio_sistema(sender, instance=None, created=False, **kwargs):
    if not created:
        return

    procedimentos = Procedimento.objects.filter(sistema=instance.sistema)
    for procedimento in procedimentos:
        EdificioProcedimento.objects.create(
            edificio=instance.edificio, sistema=instance.sistema, procedimento=procedimento, ativo=False,
        )


class EdificioProcedimento(PmModelEdificio):
    sistema = models.ForeignKey(to='sistema.Sistema', on_delete=models.CASCADE)
    procedimento = models.ForeignKey(to='sistema.Procedimento', on_delete=models.CASCADE)
    ativo = models.BooleanField()

    def __str__(self):
        return ''

    class Meta:
        db_table = 'edificio_edificio_procedimento'
        verbose_name = _('procedimento do edifício')
        verbose_name_plural = _('procedimentos do edifício')

@receiver(models.signals.post_save, sender=EdificioProcedimento)
def post_save_edificio_procedimento(sender, instance=None, created=None, **kwargs):
    if not instance.ativo:
        return

    edificio_sistema = EdificioSistemas.objects.get(edificio=instance.edificio, sistema=instance.sistema)

    situacao_criacao_manutencao = ConfigEdificio.get_config().situacao_criacao_manutencao
    datas = instance.procedimento.periodo.get_datas(edificio_sistema.inicio, edificio_sistema.final)
    for i, data in enumerate(datas):
        Manutencao.objects.create(
            edificio=instance.edificio,
            edificio_procedimento=instance,
            situacao=situacao_criacao_manutencao,
            indice=i + 1,
            data=data,
        )
