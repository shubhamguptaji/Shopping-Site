from django.db import models

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=200)


class SubCategory(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subCategory_name = models.CharField(max_length=200)
    subCategory_image = models.ImageField()


class Products(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    product_brandName = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_discount = models.DecimalField(max_digits=12, decimal_places=2)
    product_image1 = models.ImageField()
    product_image2 = models.ImageField()
    product_image3 = models.ImageField()
    product_image4 = models.ImageField()
    product_image5 = models.ImageField()
    product_specs = models.TextField(max_length=8000)
    product_sellerName = models.CharField(max_length=200)
    product_sellerAddress = models.CharField(max_length=300)
    product_sellerPhoneNo = models.CharField(max_length=13)
    product_sellerID = models.PositiveIntegerField()
    product_quantity = models.PositiveIntegerField(default=0)