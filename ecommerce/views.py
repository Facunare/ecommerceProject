from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import stockProducts, categorias
from . import forms
from ecommerce import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error': 'Usuario existente'
                })
        else:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:

            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': "El usuario o contraseña es incorrecto"
            })
        else:
            login(request, user)
            return redirect('home')
        
    
@login_required
def addStock(request):
    if request.method == 'GET':
        return render(request, 'addProduct.html', {
            'form' : forms.stockForm
        })
    else:
        print(request.POST)
        print(models.categorias.objects.get(id=request.POST['categoria']))
        stockProducts.objects.create(nom_prod=request.POST['nom_prod'], cant_prod=request.POST['cant_prod'], precio_prod=request.POST['precio_prod'], descripcion=request.POST['descripcion'],
        categoria=models.categorias.objects.get(id=request.POST['categoria']))
        return redirect('/')

@login_required
@staff_member_required
def buy(request):
    stock = stockProducts.objects.all()
    return render(request, 'buy.html', {
        'products' : stock
    })