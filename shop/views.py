from django.shortcuts import render

from shop.models import Product


# Create your views here.


def detail(request, id):
    detail = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'detail': detail})
