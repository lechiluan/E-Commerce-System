# Generated by Django 4.1.7 on 2023-03-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_contact_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
