from django.contrib import admin
from .models import Category, Product


admin.site.register(Product)
admin.site.register(Category)
# Register your models here.
# TODO admin for products
# TODO select for category in products
# TODO filtering in categories