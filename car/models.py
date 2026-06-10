from django.db import models
from brand.models import Brand
from accounts.models import Account
from django.contrib.auth.models import User


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cars/", blank=True, null=True)
    model_name = models.CharField(max_length=150)
    cc = models.IntegerField()
    release_year = models.IntegerField()
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()


    def __str__(self):
        return f"{self.brand.name}-{self.model_name}"

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
