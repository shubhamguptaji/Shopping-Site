from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello world!")

def categories(request):
    return HttpResponse("Categories")

def subCategory(request, category):
    return HttpResponse("this is subcategory of  " + category)