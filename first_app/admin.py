from django.contrib import admin
from first_app.models import Product_Details

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
admin.site.register(Product_Details,ProductAdmin)
