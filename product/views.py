from django.shortcuts import render
from .models import Product
# Create your views here.
def productPageFunction(request):
    allProducts = Product.objects.all()
    return render(request, 'e_comm/e_comm_index.html', {'allProducts': allProducts})

def checkoutPageFunction(request):
    return render(request, 'e_comm/checkout.html')