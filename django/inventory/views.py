from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Product, Supplier
from store.views import ProductListView
@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    context = {
        'products': total_product,
        'product' : Product.objects.all()
    }
    return render(request, 'dashboard.html', context)