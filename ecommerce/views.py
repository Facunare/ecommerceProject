from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import stockProducts,  carrito
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

        stockProducts.objects.create(image_prod=request.POST['image_prod'], nom_prod=request.POST['nom_prod'], cant_prod=request.POST['cant_prod'], precio_prod=request.POST['precio_prod'], descripcion=request.POST['descripcion'],
        categoria=models.categorias.objects.get(id=request.POST['categoria']))

        return redirect('buy')


@login_required
def buy(request):
    busqueda = request.GET.get("buscar")

    stock = stockProducts.objects.all()

    if busqueda:
        stock = stockProducts.objects.filter(
            nom_prod__icontains = busqueda
        )
    return render(request, 'buy.html', {
        'products' : stock
    })

@login_required 
@staff_member_required
def delete_prod(request, prod):
    
    product = get_object_or_404(stockProducts, nom_prod=prod)
    if request.method == 'POST':
        
        product.delete()
        return redirect('buy')

def addCart(request, prod):
    cantidad = request.GET.get("cant")
    product = get_object_or_404(stockProducts, pk=prod)
    
    carrito.objects.create(nom_prod = product.nom_prod, cant_prod=int(cantidad), precio_prod = product.precio_prod*int(cantidad))
    
    return redirect('buy')

def cart(request):
    total = 0
    prods = carrito.objects.all()
    for prod in prods:
        total += prod.precio_prod
    print(total)
    print(prods)
    
    return render(request, 'addToCart.html',{
        'prods': prods,
        'total': total
    })