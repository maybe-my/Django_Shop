from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
        

class Tovar(models.Model):
    top = models.BooleanField(default=False, help_text='Показать на главной странице', verbose_name='Топ товар')
    category = models.ForeignKey(Category, related_name='Товар', on_delete=models.CASCADE, default='Без категории')
    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    # Date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Image
    image_main = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=False)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    

    # размеры
    sizes = models.TextField(blank=True)
    one_size = models.BooleanField(default=False)
    S = models.BooleanField(default=False)
    M = models.BooleanField(default=False)
    L = models.BooleanField(default=False)
    XL = models.BooleanField(default=False)
    XXL = models.BooleanField(default=False)
    XXXL = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug', 'top', 'category'),)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №{}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Товар')
    product = models.ForeignKey(Tovar, related_name='Товар', on_delete=models.CASCADE, verbose_name='Товар', db_tablespace=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')

    def __str__(self):
        return '{} - товар заказали'.format(self.id)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'