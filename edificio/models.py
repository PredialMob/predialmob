import uuid
import json

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
    validade = models.DateField()

    def __str__(self):
        return self.edificio.nome + ' - ' + self.sistema.nome

    class Meta:
        db_table = 'edificio_edificio_sistemas'
        verbose_name = _('edifício sistema')
        verbose_name_plural = _('edifícios sistemas')

@receiver(models.signals.post_save, sender=EdificioSistemas)
def pre_save_edificio_sistema(sender, instance=None, created=False, **kwargs):
    try:
        if not created:
            return

        procedimentos = Procedimento.objects.filter(sistema=instance.sistema)
        for procedimento in procedimentos:
            datas = procedimento.periodo.get_datas(instance.validade)
            for i, data in enumerate(datas):
                Manutencao.objects.create(
                    edificio=instance.edificio,
                    sistema_edificio=instance,
                    procedimento=procedimento,
                    situacao=ConfigEdificio.get_config().situacao_criacao_manutencao,
                    indice=i + 1,
                    data=data,
                )
    except ImportError as e:
        from core.models import SignalsLog
        SignalsLog.objects.create(classe=type(e), exception=str(e), json=json.dumps(instance))
