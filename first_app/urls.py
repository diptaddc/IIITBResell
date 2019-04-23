from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'first_app'

urlpatterns = [
    url(r"profile/$", views.profile, name='profile'),
    url(r'^search/$', views.search , name='search'),
    url(r"product_data/$",views.form_name_view,name='product_data'),
    url(r"product_list/$",views.product_list,name='product_list'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("products_new/<int:myid>", views.productView_new, name="Prod"),
    path("products_category/<str:mycat>",views.productCat,name="ProdCat"),
    url(r'first_app/(?P<pk>[0-9]+)/delete/$', login_required(views.ProductDelete.as_view()), name='product-delete'),
]
