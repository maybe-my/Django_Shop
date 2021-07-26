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
    category = models.ForeignKey(Category, related_name='Товар', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    # Date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Image
    image_main = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    

    # размеры
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