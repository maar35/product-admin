# Generated by Django 3.2.9 on 2021-11-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAdmin', '0002_auto_20211105_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='no-product', max_length=32, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=999999.99, max_digits=16),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
