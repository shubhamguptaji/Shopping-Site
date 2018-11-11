from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Categories, Products, SubCategory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    categories = get_list_or_404(Categories)
    """ find out how many times user visits this page"""
    subcategories= []
    indexCategories = []
    for i in range(3):
        indexCategories.append(categories[i])
    for category in categories:
        subcategory = SubCategory.objects.filter(category__category_name=category.category_name)
        subcategories.append(subcategory)
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1
    # print(num_visits)
    return render(request, 'Website/index.html', {'indexCategories' : indexCategories, 'subcategories': subcategories, 'categories': categories, 'username': request.user.username})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print ("valid")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            subject = "Account Confirmation"
            message = "Confirm your email"
            from_email = settings.EMAIL_HOST_USER
            to_list = username

            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else: 
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/signup.html', context)

def discounts(request):

    return HttpResponse("Discounts Page")

def categories(request):
    categories = get_list_or_404(Categories)
    return render(request, 'Website/categories.html', {'categories' : categories})

def subCategory(request, category_name):
    category1 = get_list_or_404(Categories, category_name = category_name)
    subcategories = SubCategory.objects.filter(category__category_name=category_name)
    return render(request, 'Website/subcategories.html', {'category': category1[0], 'subcategories': subcategories})

def getProduct(request, category_name, subCategory_name):
    category = Categories.objects.filter(category_name=category_name)
    subCategory = SubCategory.objects.filter(category__category_name=category_name)
    products = Products.objects.filter(subcategory__subCategory_name=subCategory_name)
    data = {
        'category': category_name,
        'subCategory': subCategory_name,
        'products': products
    }
    return render(request, 'Website/products.html', data)

def getSpecificProduct(request, category_name, subCategory_name, product_id):
    product = get_object_or_404(Products, pk=product_id)
    data = {
        'category': category_name,
        'subcategory': subCategory_name,
        'product': product
    }
    return render(request, 'Website/specificProduct.html', data)

def myProfile(request):
    return HttpResponse("hello")