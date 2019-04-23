from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

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


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product_Details, blank=True)


    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = UserProfile.objects.get_or_create(user=instance)
    user_profile.save()

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
