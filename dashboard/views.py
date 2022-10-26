from core.views import PmTemplateView
from dashboard.widgets import NotificacoesWidget, MensagensWidget, CalendarioWidget, WidgetSistemaResumo


class DashboardView(PmTemplateView):
    template_name = 'dashboard/index.html'

    widget_notificacoes = NotificacoesWidget()
    widget_mensagens = MensagensWidget()
    widget_calendario = CalendarioWidget()

    def get_sistemas(self):
        sistemas = self.request.user.edificio.sistemas.all()
        widgets = []
        for sistema in sistemas:
            widgets.append(WidgetSistemaResumo(sistema))
        return widgets
