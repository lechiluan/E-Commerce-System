# Generated by Django 4.1.7 on 2023-03-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cartitem_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaddress',
            name='country',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
