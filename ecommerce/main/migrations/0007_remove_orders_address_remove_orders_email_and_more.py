# Generated by Django 4.1.7 on 2023-03-16 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_created_date_product_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='mobile',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coupon'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='delivery_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.deliveryaddress'),
        ),
        migrations.AddField(
            model_name='orders',
            name='total_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
