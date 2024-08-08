from django.shortcuts import render, redirect
from .models import Wine
from .forms import WineForm
from .utils import geocode_location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('wine-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def wine_index(request):
    query = request.GET.get('q', '')
    wines = request.user.wine_set.all()
    if query:
        # Filter wines based on search query
        wines = wines.filter(
            producer__icontains=query
        ) | wines.filter(
            variety__icontains=query
        ) | wines.filter(
            year__icontains=query
        ) | wines.filter(
            style__icontains=query
        ) | wines.filter(
            country__icontains=query
        ) | wines.filter(
            region__icontains=query
        )
    
    if request.headers.get('HX-Request'):
        return render(request, 'wines/_wine_list.html', {'wines': wines})    
    return render(request, 'wines/index.html', {'wines': wines})

class WineCreate(LoginRequiredMixin, CreateView):
    model = Wine
    form_class = WineForm
    template_name = 'core/wine_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def wine_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    coordinates = geocode_location(wine.country, wine.region)
    if not coordinates:
        coordinates = [-74.5, 40]
    return render(request, 'wines/detail.html', {'wine': wine, 'coordinates': coordinates})

class WineUpdate(LoginRequiredMixin, UpdateView):
    model = Wine
    form_class = WineForm
    template_name = 'core/wine_form.html'

class WineDelete(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = '/wines/'