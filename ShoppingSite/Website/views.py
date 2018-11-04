from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Categories, Products, SubCategory

# Create your views here.

def home(request):
    categories = get_list_or_404(Categories)
    return render(request, 'Website/index.html', {'categories' : categories})

def discounts(request):
    return HttpResponse("Discounts Page")

def categories(request):
    return HttpResponse("Categories")

def subCategory(request, category):
    return HttpResponse("this is subcategory of  " + category)

def getProduct(request, category, subCategory):
    return HttpResponse("this is a product of  category: " + category);

def getSpecificProduct(request, category, subCategory, product_id):
    return HttpResponse("hello")