from django.shortcuts import render,redirect
from first_app.forms import ProductForm
from accounts.forms import CustomUserCreationForm
from django.core.files.storage import FileSystemStorage
from . import forms
from first_app.models import Product_Details,Images
from math import ceil
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.conf import settings
from django.db.models import Count

# Create your views here.
from django.http import HttpResponse

@login_required()
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
    imeg= Images.objects.filter(post=products[0])
    x=imeg.count()
    print(x)
    image_url=settings.MEDIA_URL
    print(image_url)
    url=[]
    for i in range(0,x):
        image=image_url+'/'+imeg[i].image.name
        print(image)
        url.append(image)
    params = {'product' : products[0],
    'images':url,
    }
    print(products[0].Price)
    return render(request, 'first_app/productView_new.html', params)

@login_required()
def form_name_view(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            for f in formset:
                try:
                    photo=Images(post=post,image=f.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break
        return redirect('product_list')

    else:
        form = ProductForm()
        formset = ImageFormset(queryset=Images.objects.none())

    context={
    'form':form,
    'formset':formset,
    }

    return render(request,"first_app/product_data.html", context)


def search(request):
    return render(request, 'first_app/images.html')
