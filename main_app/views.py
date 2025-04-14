from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Rim
from .forms import InfoForm




# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    rims = Rim.objects.all()
    info_form = InfoForm()
    return render(request, 'cars/detail.html', {
        'car': car, 
        'info_form': info_form,
        'rims': rims
        })

@login_required
def add_info(request, car_id):
    form = InfoForm(request.POST)

    if form.is_valid():

        new_info = form.save(commit=False)
        new_info.car_id = car_id
        new_info.save()
    return redirect('car-detail', car_id=car_id)

def associate_rim(request, car_id, rim_id):
    Car.objects.get(id=car_id).rims.add(rim_id)
    return redirect('car-detail', car_id=car_id)

@login_required
def remove_rim(request, car_id, rim_id):
    car = Car.objects.get(id=car_id)
    rim = Rim.objects.get(id=rim_id)
    car.rims.remove(rim_id)
    return redirect('car-detail', car_id=car.id)

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'image']

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

class RimCreate(LoginRequiredMixin, CreateView):
    model = Rim
    fields = '__all__'

class RimList(LoginRequiredMixin, ListView):
    model = Rim

class RimDetail(LoginRequiredMixin, DetailView):
    model = Rim

class RimUpdate(LoginRequiredMixin, UpdateView):
    model = Rim
    fields = ['brand', 'diameter', 'description', 'image']

class RimDelete(LoginRequiredMixin, DeleteView):
    model = Rim
    success_url = '/rims/'

def signup(request):
    error_message = ''
    if request.method == 'POST':


        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()

            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

