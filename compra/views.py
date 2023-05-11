from django.shortcuts import render, redirect
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm


# Create your views here.
def index(request):
    return render(request, 'index.jinja')

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.jinja', context)


def suppliers_list(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'suppliers.jinja', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            return redirect('/create_product/')
    else:
        form = ProductForm()

    context = {'form': form, 'element_to_create': 'Producto'}

    return render(request, 'creation.jinja', context)


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/suppliers/')
        else:
            return redirect('/suppliers/create/')
    else:
        form = SupplierForm()

    context = {'form': form, 'element_to_create': 'Proveedor'}

    return render(request, 'creation.jinja', context)
