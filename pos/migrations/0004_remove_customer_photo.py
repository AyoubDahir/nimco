# Generated by Django 4.0.5 on 2022-06-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_customer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='photo',
        ),
    ]
