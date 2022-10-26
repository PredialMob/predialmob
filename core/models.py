import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField


class PmModel(models.Model):
    alterado_em = models.DateTimeField(auto_now=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PmModelEdificio(PmModel):
    sid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    edificio = models.ForeignKey(to='edificio.Edificio', on_delete=models.CASCADE, to_field='sid')

    class Meta:
        abstract = True


def get_user_foto_filename(instance, filename):
    return 'usuario/' + str(instance.sid) + '/' + filename


class Usuario(PmModelEdificio, AbstractUser):
    foto = ImageField(upload_to=get_user_foto_filename)

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')


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


class SignalsLog(PmModel):
    classe = models.CharField(max_length=32, null=False, blank=True)
    exception = models.TextField(null=False, blank=True)
    json = models.JSONField(null=True, blank=True)
