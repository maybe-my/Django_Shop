# Generated by Django 3.2.5 on 2021-08-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0006_auto_20210822_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='kod',
            field=models.CharField(default=[2, 9, 8, 3], max_length=6),
        ),
    ]