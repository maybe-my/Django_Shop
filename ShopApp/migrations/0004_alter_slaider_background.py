# Generated by Django 3.2.5 on 2021-08-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_slaider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slaider',
            name='background',
            field=models.ImageField(blank=True, upload_to='media/slaidbar/%Y/%m/%d'),
        ),
    ]
