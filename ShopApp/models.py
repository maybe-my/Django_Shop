from django.db import models

# Категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Товары
class Tovar(models.Model):
    kod = models.CharField('Код товара',max_length=6,blank=True, default='')
    new = models.BooleanField(default=True, help_text='Показать на главной странице что товар новый', verbose_name='Новый товар')
    top = models.BooleanField(default=False, help_text='Показать на главной странице', verbose_name='Топ товар')
    familys = (
        ('o', 'Выберите пол'),
        ('m', 'Мужчинам'),
        ('w', 'Женщинам'),
        ('k', 'Детям'),
    )
    family = models.CharField('Пол', max_length=10, choices=familys, default='o')
    category = models.ForeignKey(Category,verbose_name='Категория', related_name='Товар',  default='Без категории', on_delete=models.SET_DEFAULT)
    name = models.CharField('Название', max_length=40, db_index=True)
    slug = models.SlugField('Сылка на товар', max_length=200, db_index=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена',max_digits=10, decimal_places=0)
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    available = models.BooleanField('Активно', default=True)

    # Date
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Последнее изменение', auto_now=True)

    # Image
    image_main = models.ImageField('Главное фото*', upload_to='media/products/%Y/%m/%d', blank=False)
    image1 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    

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
        verbose_name_plural = f'Товары'
        index_together = (('id', 'slug', 'top', 'category'),)

    def __str__(self):
        return self.name

    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        price = int(self.price * (100 - self.sale) / 100)
        return price


# заказы
class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50, blank=False)
    last_name = models.CharField('Фамилия', max_length=50, blank=False)
    email = models.EmailField('Почта', blank=False)
    phone = models.CharField('Номер телефона', max_length=13, blank=False)
    address = models.CharField('Адресс', max_length=250, blank=False)
    city = models.CharField('Город/обл', max_length=100, blank=False)
    comment = models.CharField('Коментарий к заказу', max_length=300, blank=True)
    paid = models.BooleanField('Оплачено', default=False)

    created = models.DateTimeField('Дата оформление заказа', auto_now_add=True)
    updated = models.DateTimeField('Последнее изменение' ,auto_now=True)
    
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id} | Имя/Фамилия: {self.first_name}/{self.last_name} | Почта: {self.email} | Номер телефона: {self.phone}'


# Заказы
class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Товар')
    product = models.ForeignKey(Tovar, related_name='Товар', on_delete=models.CASCADE, verbose_name='Товар', db_tablespace=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')

    def __str__(self):
        return '{} - товар заказали'.format(self.id)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# Слайдер
class Slaider(models.Model):
    background = models.ImageField(upload_to='media/slaidbar/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=40)
    button_title = models.CharField(max_length=15)
    button_url =  models.URLField()
    active = models.BooleanField(default=True)
    active_tovar = models.BooleanField('Показывать товар',default=False) 
    tovar = models.ForeignKey(Tovar, verbose_name='Товар', default='без товара', on_delete=models.CASCADE, null=True, blank=True)

    # Date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

# Обратная связь
class Contact(models.Model):
    name = models.CharField('Имя', max_length=30, blank=False)
    email = models.EmailField('Почта', blank=False)
    message = models.CharField('Коментарий', max_length=600, blank=False)

    # Date
    created = models.DateTimeField('Дата обращения', auto_now_add=True)
    updated = models.DateTimeField('Последнее изменение', auto_now=True)