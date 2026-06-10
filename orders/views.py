from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from .forms import OrderForm
from car.models import Car
from .models import Order
from django.shortcuts import get_object_or_404


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
