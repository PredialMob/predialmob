from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _


class CardNotificacoes:
    nao_lidas = 0

    def get_descricao(self):
        if self.nao_lidas == 1:
            return str(self.nao_lidas) +  _(' notificação não lida')
        return str(self.nao_lidas) + _(' notificações não lidas')


class NotificacoesWidget(CardNotificacoes):
    bg_color = 'bg-color-1'
    bg_icon = 'bg-icon-1'
    icon = 'bx bxs-bell bx-tada bx-tada'
    p_color = 'color-1'
    titulo = _('Notificações')

    def __init__(self):
        self.list = ListaNotificacao('Notificações')
        # self.list.append(Notificacao('Sistema 1', 'Verificar'))



class MensagensWidget(CardNotificacoes):
    bg_color = 'bg-color-2'
    bg_icon = 'bg-icon-2'
    icon = 'bx bxs-message-rounded'
    p_color = 'color-2'
    titulo = _('Mensagens')


class CalendarioWidget(CardNotificacoes):
    bg_color = 'bg-color-3'
    bg_icon = 'bg-icon-3'
    icon = 'bx bx-calendar'
    p_color = 'color-3'
    titulo = _('Calendário')
    # href = reverse_lazy('index')


class ListaNotificacao(list):

    def __init__(self, titulo):
        super().__init__()
        self.titulo = titulo


class Notificacao:

    def __init__(self, titulo, descricao=None, imagem=None, href=None):
        self.titulo = titulo
        self.descricao = descricao
        self.imagem = imagem
        self.href = href


class WidgetSistemaResumo:

    def __init__(self, sistema):
        self.sistema = sistema
        self.manutencoes_total = sistema.get_manutencoes_total()
        self.manutencoes_abertas = sistema.get_manutencoes_abertas()
        self.manutencoes_fechadas = self.manutencoes_total - self.manutencoes_abertas
        if self.manutencoes_total == 0:
            self.percentual = '100'
        else:
             self.percentual = '%.0f' % (self.manutencoes_fechadas * 100 / self.manutencoes_total)