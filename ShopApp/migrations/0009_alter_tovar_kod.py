# Generated by Django 3.2.5 on 2021-08-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0008_alter_tovar_kod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='kod',
            field=models.CharField(blank=True, default='13', max_length=6),
        ),
    ]
