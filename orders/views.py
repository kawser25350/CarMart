from django.shortcuts import render,redirect
from django.views.generic import FormView,View,ListView
from .forms import OrderForm
from car.models import Car
from .models import Order
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderView(View):
    
    def post(self,request,pk):

        car=get_object_or_404(Car,pk=pk)

        
        if car.quantity > 0 : 
            Order.objects.create(
                user=request.user,
                car=car,
                price=car.price
            )
            car.quantity-=1
            car.save()
        return redirect("car_details",pk=car.pk)

class CustomerOrderView(LoginRequiredMixin,ListView):
    model = Order
    template_name='orders/customer_orders.html'
    context_object_name='orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

