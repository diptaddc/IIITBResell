from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from first_app.models import Product_Details


def product_list(request):
    products = Product_Details.objects.all()
    return render(request, 'first_app/product_list.html', {
        'products': products
    })
