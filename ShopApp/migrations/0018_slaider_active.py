# Generated by Django 3.2.5 on 2021-07-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0017_auto_20210729_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='slaider',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
