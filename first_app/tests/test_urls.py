from django.test import SimpleTestCase
from django.urls import reverse, resolve
from first_app.views import product_list,form_name_view

class TestUrls(SimpleTestCase):


	def test_product_list_url(self):
		url = reverse('product_list')
		self.assertEquals(resolve(url).func, product_list)

	def test_product_data(self):
		url = reverse('product_data')
		self.assertEquals(resolve(url).func, form_name_view)