from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products_list, name='products-list'),
    path('products/create/', views.create_product, name='create-product'),
    path('suppliers/', views.suppliers_list, name='suppliers-list'),
    path('suppliers/create/', views.create_supplier, name='create-supplier')
]
