# Generated by Django 3.2.5 on 2021-08-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0004_alter_slaider_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShopApp.tovar'),
        ),
    ]
