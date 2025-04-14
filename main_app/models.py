from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Rim(models.Model):
    brand = models.CharField(max_length=50)
    diameter = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='rim_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.diameter}'
    
    def get_absolute_url(self):
        return reverse('rim-detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    rims = models.ManyToManyField(Rim)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
    
class Info(models.Model):
    color = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.color} {self.mileage} ({self.id})'
