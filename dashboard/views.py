from core.views import PmTemplateView
from dashboard.widgets import NotificacoesWidget, MensagensWidget, CalendarioWidget, WidgetSistemaResumo


class NotificationViewMixin:
    widget_notificacoes = NotificacoesWidget()
    widget_mensagens = MensagensWidget()
    widget_calendario = CalendarioWidget()


class ListaSistemasMixin:

    def get_sistemas(self):
        sistemas = self.request.user.edificio.sistemas.all()
        widgets = []
        for sistema in sistemas:
            widgets.append(WidgetSistemaResumo(sistema))
        return widgets


class DashboardView(PmTemplateView, NotificationViewMixin, ListaSistemasMixin):
    template_name = 'dashboard/index.html'
