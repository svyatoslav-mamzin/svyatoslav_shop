# Generated by Django 2.2.6 on 2020-11-06 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
    ]