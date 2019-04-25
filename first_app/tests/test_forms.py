
from django.test import TestCase
from first_app.forms import ProductForm

class RenewBookFormTest(TestCase):
    def test_Product_Name_label(self):
        form = ProductForm()
        self.assertTrue(form.fields['Product_Name'].label == None or form.fields['Product_Name'].label == 'Product Name')

    def test_Category_label(self):
        form = ProductForm()
        self.assertTrue(form.fields['Category'].label == None or form.fields['Category'].label == 'Category')

