# Generated by Django 4.1.1 on 2022-10-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_stockproducts_image_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproducts',
            name='image_prod',
            field=models.ImageField(upload_to='ecommerce/photos'),
        ),
    ]
