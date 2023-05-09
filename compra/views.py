from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.jinja', context)


def suppliers_list(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'suppliers.jinja', context)


def create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return HttpResponseRedirect('/create_product/')

    context = {'form': form}

    return render(request, 'create_product.jinja', context)


def create_supplier(request):
    form = SupplierForm()

    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return HttpResponseRedirect('/create_supplier.jinja/')

    context = {'form': form}

    return render(request, 'create_supplier.jinja', context)
