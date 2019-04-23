from django.contrib import admin
from first_app.models import Product_Details,Images,UserProfile

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(UserProfile)

admin.site.register(Product_Details,ProductAdmin)
admin.site.register(Images, ImagesAdmin)
