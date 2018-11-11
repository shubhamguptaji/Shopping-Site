from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('discounts/', views.discounts, name="discounts"),
    path('categories/', views.categories, name='categories'),
    path('<category_name>/subcategory/', views.subCategory, name='subCategory'),
    path('<category_name>/<subCategory_name>/', views.getProduct, name='getProduct'),
    path('myProfile/', views.myProfile, name='myProfile'),
    # path('<category_name>/<subCategory_name>/products/<product_id>/', views.getSpecificProduct, name='getSpecificProduct'),
]