from django.db import models
from django.conf import settings
# Create your models here.


Category_Choice = (
    ('sport','SPORT'),
    ('electronic', 'ELECTRONIC'),
    ('other','OTHER')
)


class Product_Details(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True,on_delete=models.SET_NULL)
    Product_Name=models.CharField(max_length=120)
    Category=models.CharField(max_length=120,choices=Category_Choice, default='other')
    Brand=models.CharField(max_length=120,default='null')
    Title=models.CharField(max_length=120,default='null')
    Description=models.TextField(blank=True, null=True)
    Price=models.PositiveIntegerField()
    Negotiation=models.CharField(max_length=120)
    Picture=models.ImageField(null=True,blank=True)


    def __str__(self):
        return str(self.id)


class Images(models.Model):
    post = models.ForeignKey(Product_Details,null=True, blank=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images',null=True)
    

    def __str__(self):
        return str(self.image.name)
