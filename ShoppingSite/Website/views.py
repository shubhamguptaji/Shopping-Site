from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Categories, Products, SubCategory

def home(request):
    categories = get_list_or_404(Categories)
    """ find out how many times user visits this page"""
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    print(num_visits)
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
    category = Categories.objects.filter(category_name=category)
    subCategory = SubCategory.objects.filter(category__category_name=category.category_name)
    products = Products.objects.filter(subCategory__subCategory_name=subCategory.subCategory_name)
    return HttpResponse("this is a product of  category: " + category);

def getSpecificProduct(request, category, subCategory, product_id):
    return HttpResponse("hello")