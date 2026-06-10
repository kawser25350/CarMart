from django.views.generic import TemplateView
from brand.models import Brand
from car.models import Car


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['brands'] = Brand.objects.all()
        cars = Car.objects.all()
        
        selected_brand = self.request.GET.get('brand')

        if selected_brand:
            cars = cars.filter(brand__name=selected_brand)

        context['cars'] = cars
        return context

