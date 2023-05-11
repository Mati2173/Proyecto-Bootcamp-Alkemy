from django import forms
from .models import Product, Supplier


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {'name': 'Nombre',
                  'price': 'Precio',
                  'current_stock': 'Stock Actual',
                  'supplier': 'Proveedor'}


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'
        labels = {'first_name': 'Nombre',
                  'surname': 'Apellido',
                  'dni': 'DNI'}

