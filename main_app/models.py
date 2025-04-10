from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.make} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
