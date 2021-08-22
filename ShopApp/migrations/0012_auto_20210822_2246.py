# Generated by Django 3.2.5 on 2021-08-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0011_auto_20210822_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('comment', models.CharField(max_length=600, verbose_name='Коментарий к заказу')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма заказа'),
        ),
    ]