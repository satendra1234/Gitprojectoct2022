from account.models import Profile
from django.contrib import admin
from product.models import Category, Product, ProductImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Profile)

