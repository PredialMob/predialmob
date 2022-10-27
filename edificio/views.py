from core.views import PmDetailView
from dashboard.views import ListaSistemasMixin, NotificationViewMixin
from edificio.models import Edificio


class EdificioDetailView(PmDetailView, NotificationViewMixin, ListaSistemasMixin):
    template_name = 'edificio/edificio.html'
    model = Edificio
    slug_field = 'sid'
    slug_url_kwarg = 'sid'

    def get_object(self, queryset=None):
        return super().get_object(queryset)