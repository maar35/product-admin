# Generated by Django 3.2.9 on 2021-11-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAdmin', '0003_auto_20211105_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='question_text',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='choice',
            name='customer_name',
            field=models.CharField(default='no-customer', max_length=72),
        ),
        migrations.AddField(
            model_name='choice',
            name='shipping_address',
            field=models.CharField(default='no-address', max_length=300),
        ),
    ]