# Generated by Django 3.2.5 on 2021-07-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_auto_20210726_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='top',
            field=models.BooleanField(default=False, help_text='Показать на главной странице'),
        ),
    ]
