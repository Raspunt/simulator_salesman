# Generated by Django 4.1.1 on 2022-09-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game_Main', '0006_remove_product_amount_product_amountkg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='telega_products',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='telega_weightkg',
            new_name='weightkg',
        ),
    ]