# Generated by Django 2.2.6 on 2020-11-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'article')},
            },
        ),
    ]
