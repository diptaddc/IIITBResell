from django.shortcuts import render,redirect
from first_app.forms import ProductForm
from django.core.files.storage import FileSystemStorage
from . import forms
from .models import Product_Details
from math import ceil

# Create your views here.
from django.http import HttpResponse


def product_list(request):
    #products = Product_Details.objects.all()
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    #return render(request, 'first_app/product_list.html', params)

    allProds = []
    catprods = Product_Details.objects.values('Category', 'id')
    cats = {item['Category'] for item in catprods}
    for cat in cats:
        prod = Product_Details.objects.filter(Category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'first_app/product_list.html', params)


def productView(request, myid):
    # Fetch the product using the id
    products = Product_Details.objects.filter(id=myid)
    params = {'product' : products[0]}
    print(products[0].Price)
    return render(request, 'first_app/prodView.html', params)

def productView_new(request,myid):
    products = Product_Details.objects.filter(id=myid)
    params = {'product' : products[0]}
    print(products[0].Price)
    return render(request, 'first_app/productView_new.html', params)


def form_name_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request,"first_app/product_data.html", {'form': form})
