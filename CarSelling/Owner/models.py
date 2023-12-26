from django.db import models
from Car.models import carmodel

# Create your models here.
class profileModel(models.Model):
    Owner_Name = models.CharField(max_length= 100)
    owner = models.ForeignKey(carmodel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Owner_Name