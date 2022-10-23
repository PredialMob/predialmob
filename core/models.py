import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext as _


class PmModel(models.Model):
    sid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    alterado_em = models.DateTimeField(auto_now=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PmModelEdificio(PmModel):
    edificio = models.ForeignKey(to='edificio.Edificio', on_delete=models.CASCADE, to_field='sid')

    class Meta:
        abstract = True


class Usuario(PmModelEdificio, AbstractUser):
    pass


@receiver(models.signals.pre_save, sender=Usuario)
def pre_save_superuser(sender, instance=None, created=False, **kwargs):
    if not instance.is_superuser:
        return

    from edificio.models import Edificio
    edificios = Edificio.objects.all()
    if len(edificios) > 0:
        instance.edificio = edificios[0]
    else:
        instance.edificio = Edificio.objects.create(nome='Edifício Padrão')


class DescricaoMixin(models.Model):
    descricao_length = 240
    descricao_unique = False
    descricao_verbose = _('descrição')

    descricao = models.CharField(max_length=descricao_length, unique=descricao_unique, verbose_name=descricao_verbose)

    def __str__(self):
        return self.descricao

    class Meta:
        abstract = True
