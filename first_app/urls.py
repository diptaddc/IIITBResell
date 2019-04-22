from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r"product_data/$",views.form_name_view,name='form_name'),
    url(r"product_list/$",views.product_list,name='product_list'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("products_new/<int:myid>", views.productView_new, name="Prod"),
    url(r'first_app/(?P<pk>[0-9]+)/delete/$', login_required(views.ProductDelete.as_view()), name='product-delete'),

]
