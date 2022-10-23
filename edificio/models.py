from django.db import models
from django.utils.translation import gettext as _

from core.models import PmModel, PmModelEdificio


class Edificio(PmModel):
    nome = models.CharField(max_length=120)
    sistemas = models.ManyToManyField(to='sistema.Sistema', through='EdificioSistemas')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('edifício')


class EdificioSistemas(PmModelEdificio):
    sistema = models.ForeignKey(to='sistema.Sistema', on_delete=models.CASCADE)

    class Meta:
        db_table = 'edificio_edificio_sistemas'
        verbose_name = _('edifício sistema')
        verbose_name_plural = _('edifícios sistemas')
