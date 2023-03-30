from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)