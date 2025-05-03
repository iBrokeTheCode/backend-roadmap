from django.shortcuts import render

from products.models import Product


def homepage(request):
    return render(request, 'products/index.html')


def product_list(request):
    context = {'products': Product.objects.all()}

    return render(request, 'products/product_list.html', context)
