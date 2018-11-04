from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discounts/', views.discounts, name="discounts"),
    path('categories/', views.categories, name='categories'),
    path('<category>/subcategory/', views.subCategory, name='subCategory'),
    path('<category>/<subCategory>/products/', views.getProduct, name='getProduct'),
    path('<category>/<subCategory>/products/<product_id>/', views.getSpecificProduct, name='getSpecificProduct'),
]