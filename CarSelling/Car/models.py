from django.db import models
from Brand.models import brandmodel

# Create your models here.
class carmodel(models.Model):
    Car_Name = models.CharField(max_length= 100)
    Car_Model = models.IntegerField()
    Brand = models.ForeignKey(brandmodel, on_delete= models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to= 'Car/media/uploads/', blank= True, null= True)
    # slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    def __str__(self):
        return self.Car_Name
    
    
class Comment(models.Model):
    car = models.ForeignKey(carmodel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"