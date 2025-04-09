from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.make} ({self.id})'
