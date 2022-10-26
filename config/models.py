from django.db import models
from django.utils.translation import gettext as _

from core.models import PmModel, PmModelEdificio


class ConfigForeignKey(models.ForeignKey):

    def __init__(self, to, verbose_name, help_text, *args, **kwargs):
        super().__init__(to=to, on_delete=models.SET_NULL, null=True, blank=True,
                         verbose_name=verbose_name, help_text=help_text)


class ConfigMixin:

    @classmethod
    def get_config(cls):
        return cls.objects.all()[0]


class ConfigGeral(PmModel, ConfigMixin):

    class Meta:
        verbose_name = _('configuração geral')
        verbose_name_plural = _('configurações gerais')


class ConfigEdificio(PmModelEdificio, ConfigMixin):
    situacao_criacao_manutencao = ConfigForeignKey(
        to='programa.Situacao',
        verbose_name=_('Situação para criação automática de manutenção'),
        help_text='edificio.models.pre_save_edificio_sistema'
    )

    def __str__(self):
        return _('Configuração de ') + self.edificio.nome

    class Meta:
        verbose_name = _('configuração por edifício')
        verbose_name_plural = _('configurações por edifício')
