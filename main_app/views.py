from django.shortcuts import render


# Create your views here.

class Car:
    def __init__(self, make, model, year, image):
        self.make = make
        self.model = model
        self.year = year
        self.image = image 

cars = [
    Car('Dodge', 'Ram', '2024', 'No Current Image'),
    Car('Chevorlet', 'Silverado', '2023', 'No Current Image'),
    Car('Chevorlet', 'SS Impala', '1996', 'No Current Image')
]
        

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    return render(request, 'cars/index.html', {'cars': cars})
