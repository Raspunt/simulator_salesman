# Generated by Django 4.1.1 on 2022-09-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game_Main', '0003_events_dealer_money_dealer_telega_weightkg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]