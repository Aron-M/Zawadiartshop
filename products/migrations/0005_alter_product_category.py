# Generated by Django 4.2.4 on 2023-08-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('paintings', 'Paintings'), ('sculptures', 'Sculptures'), ('frames', 'Frames'), ('crafts', 'Crafts')], max_length=20),
        ),
    ]