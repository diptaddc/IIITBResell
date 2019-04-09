from django.conf.urls import url
from . import views

app_name = 'first_app'

urlpatterns = [
    url(r"product_data/$",views.form_name_view,name='form_name'),
    url(r"product_list/$",views.product_list,name='product_list'),
]
