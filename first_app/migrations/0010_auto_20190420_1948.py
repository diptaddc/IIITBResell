# Generated by Django 2.1.7 on 2019-04-20 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_product_details_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(null=True, upload_to='product/img/'),
        ),
    ]