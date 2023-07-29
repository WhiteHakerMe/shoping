import random
import numpy as np
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(requests):
    ctg = Category.objects.all()
    sneaker = Sneakers.objects.all()
    Recklama = recklama.objects.all()
    Recklama_r = random.choice(Recklama)
    ctx = {
        'ctg':ctg,
        'sneaker':sneaker,
        'Recklama_r':Recklama_r,
    }
    return render(requests, "blog/index.html", ctx)

def contact(requests):
    ctx = {}
    return render(requests, "blog/contact.html", ctx)

def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg':ctg,
        'category':category,
        'sneaker':sneaker,
    }
    return render(requests, "blog/products.html", ctx)

def register(requests):
    ctx = {}
    return render(requests, "blog/register.html", ctx)

def single(requests, pk=None):
    ctg = Category.objects.all()
    sneakers = Sneakers.objects.all()
    random_s = np.random.choice(sneakers, size=6, replace=False)
    products_pk = Sneakers.objects.get(pk=pk)
    form = ChoiceForm()
    if requests.POST:
        form = ChoiceForm(requests.POST or None,
                          requests.FILES or None)
        if form.is_valid():
            root = form.save()
            root = Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        'ctg':ctg,
        'product_pk':products_pk,
        'form':form,
        'random_s':random_s,
        'sneakers':sneakers,
    }
    
    return render(requests, "blog/single.html", ctx)