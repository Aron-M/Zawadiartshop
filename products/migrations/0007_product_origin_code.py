# Generated by Django 4.2.4 on 2023-08-23 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=3),
            preserve_default=False,
        ),
    ]
