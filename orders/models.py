from django.db import models
from accounts.models import Account
from car.models import Car

class Order(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    price=models.IntegerField()
    date_time=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.user.first_name}-{car.model_name}-{car.Brand.name}"







    