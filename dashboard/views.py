from core.views import PmTemplateView
from dashboard.widgets import NotificacoesWidget, MensagensWidget, CalendarioWidget


class DashboardView(PmTemplateView):
    template_name = 'dashboard/index.html'

    widget_notificacoes = NotificacoesWidget()
    widget_mensagens = MensagensWidget()
    widget_calendario = CalendarioWidget()
