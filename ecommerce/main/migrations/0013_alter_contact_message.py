# Generated by Django 4.1.7 on 2023-03-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_date_contact_date_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
