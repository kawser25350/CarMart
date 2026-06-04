

from django.views.generic import TemplateView
from brand.models import Brand

class HomeView(TemplateView):
    template_name='home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context