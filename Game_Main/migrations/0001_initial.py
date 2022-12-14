# Generated by Django 4.1.1 on 2022-09-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_product', models.CharField(max_length=100)),
                ('freshness', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delerName', models.CharField(max_length=100)),
                ('telegaName', models.CharField(max_length=100)),
                ('telega_products', models.ManyToManyField(to='Game_Main.product')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(to='Game_Main.product')),
            ],
        ),
    ]
