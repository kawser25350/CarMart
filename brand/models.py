from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=150)
    founder = models.CharField(max_length=150)
    founded = models.DateField()

    def __str__(self):
        return self.name