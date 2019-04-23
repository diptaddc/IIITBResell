from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from first_app.models import Product_Details
from first_app.forms import ProductForm
from math import ceil
from django.contrib.auth.decorators import login_required
from first_app.models import Product_Details,Images,UserProfile

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


@login_required()
def form_name_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request,"first_app/product_data.html", {'form': form})


@login_required()
def profile(request):
    my_user_profile = UserProfile.objects.filter(user=request.user.id).first()
    print(my_user_profile)
    products = Product_Details.objects.filter(user=my_user_profile.user.id)
    context = {
    	'products': products
    }
    return render(request, "first_app/home.html", context)


@login_required()
def search(request):
    if request.method == 'POST':
        Product_name =  request.POST.get('search')
        print(Product_name)
        try:
            status = Product_Details.objects.filter(Product_Name__icontains=Product_name)
        except Product_Details.DoesNotExist:
            status = None
        return render(request,"first_app/search.html",{"product_list":status})
    else:
        return render(request,"first_app/search.html")
