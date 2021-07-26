# Generated by Django 3.2.5 on 2021-07-26 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0011_remove_orders_tovar'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='tovar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Товар', to='ShopApp.tovar'),
            preserve_default=False,
        ),
    ]
