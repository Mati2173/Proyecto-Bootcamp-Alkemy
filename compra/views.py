from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Supplier


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    cxt = {'products': products}
    return render(request, 'products.jinja', cxt)


def suppliers_list(request):
    suppliers = Supplier.objects.all()
    cxt = {'suppliers': suppliers}
    return render(request, 'suppliers.jinja', cxt)


def create_product(request):
    pass


def create_supplier(request):
    pass
