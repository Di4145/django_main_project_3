from django.contrib import admin

from shop.models import Type, Maker, Product

# Register your models here.
admin.site.register(Type)
admin.site.register(Maker)
admin.site.register(Product)