from django.db import models
from django.contrib.auth.models import User
from car.models import Car

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    price=models.IntegerField()
    date_time=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}-{self.car.model_name}-{self.car.brand.name}"







    