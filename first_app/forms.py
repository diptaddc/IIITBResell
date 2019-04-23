from first_app.models import Product_Details
from django import forms

class ProductForm(forms.ModelForm):
    class Meta():
        model=Product_Details
        fields=("Product_Name","Category","Brand","Title","Description","Price","Negotiation","Picture")
