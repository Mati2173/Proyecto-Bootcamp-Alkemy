from django.contrib import admin
from .models import Product, Supplier


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'current_stock', 'supplier')
    list_filter = ('supplier',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'dni')
    search_fields = ('dni',)


admin.site.register(Supplier, SupplierAdmin)
