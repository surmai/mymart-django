from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

#shows all the products available on the index page
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})