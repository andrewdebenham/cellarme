from django.shortcuts import render, redirect
from .models import Wine
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
    wines = request.user.wine_set.all()
    return render(request, 'wines/index.html', {'wines': wines})

class WineCreate(LoginRequiredMixin, CreateView):
    model = Wine
    fields = ['producer', 'variety', 'year', 'style', 'country', 'region', 'months']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def wine_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    return render(request, 'wines/detail.html', {'wine': wine})

class WineUpdate(LoginRequiredMixin, UpdateView):
    model = Wine
    fields = ['producer', 'variety', 'year', 'style', 'country', 'region', 'months']

class WineDelete(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = '/wines/'