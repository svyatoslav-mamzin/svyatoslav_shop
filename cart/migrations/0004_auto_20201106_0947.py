# Generated by Django 2.2.6 on 2020-11-06 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20201106_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='order',
            new_name='cart',
        ),
    ]
