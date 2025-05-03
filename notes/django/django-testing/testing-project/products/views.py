from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.forms import ProductForm
from products.models import Product


def homepage(request):
    return render(request, 'products/index.html')


def product_list(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('products:product-list')
        else:
            context = {'products': Product.objects.all(), 'form': form}
            return render(request, 'products/product_list.html', context)

    context = {'products': Product.objects.all(), 'form': ProductForm()}

    return render(request, 'products/product_list.html', context)


@login_required()
def profile_view(request):
    return render(request, 'products/profile.html')


def login_view(request):
    return render(request, 'products/login.html')
