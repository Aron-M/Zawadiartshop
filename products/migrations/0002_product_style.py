# Generated by Django 4.2.4 on 2023-08-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
    ]
