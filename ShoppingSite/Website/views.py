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
    categories = get_list_or_404(Categories)
    return render(request, 'Website/categories.html', {'categories' : categories})

def subCategory(request, category):
    category1 = get_list_or_404(Categories, category_name = category)
    subcategories = SubCategory.objects.filter(category__category_name=category)
    return render(request, 'Website/subcategories.html', {'category': category1[0], 'subcategories': subcategories})

def getProduct(request, category, subCategory):
    return HttpResponse("this is a product of  category: " + category);

def getSpecificProduct(request, category, subCategory, product_id):
    return HttpResponse("hello")