# Generated by Django 4.2.4 on 2023-08-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]