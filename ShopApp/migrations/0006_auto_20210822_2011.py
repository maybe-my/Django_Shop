# Generated by Django 3.2.5 on 2021-08-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0005_tovar_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='parent_category',
        ),
        migrations.AddField(
            model_name='tovar',
            name='kod',
            field=models.CharField(default=[9, 8, 6, 2], max_length=6),
        ),
    ]
