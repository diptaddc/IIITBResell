from django.db import models

# Create your models here.


Category_Choice = (
    ('sport','SPORT'),
    ('electronic', 'ELECTRONIC'),
    ('other','OTHER')
)

class Product_Details(models.Model):
    Product_Name=models.CharField(max_length=120)
    Category=models.CharField(max_length=120,choices=Category_Choice, default='other')
    Description=models.CharField(max_length=120)
    Price=models.PositiveIntegerField()
    Negotiation=models.CharField(max_length=120)
    Picture=models.ImageField(upload_to='product/img/',null=True)

    def __str__(self):
        return self.Product_Name
