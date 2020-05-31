from django.shortcuts import render
from .models import Product
# Create your views here.

def productList(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', { 'products': products})