from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name="products-list"),
    path('suppliers/', views.suppliers_list, name="suppliers-list"),
    path('create_product/', views.create_product, name='create-product'),
    path('create_supplier/', views.create_supplier, name='create-supplier')
]
