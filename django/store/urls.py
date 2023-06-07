from django.urls import path

from .views import (
    create_supplier,
    create_product,
    SupplierListView,
    ProductListView,
    update_product,
    ProductDetailView,
    purchase_product,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-product/', create_product, name='create-product'),
    path('update-product/<int:pk>/', update_product, name='update-product'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buy-product/<int:pk>/', purchase_product, name='purchase-product'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
]
