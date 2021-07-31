from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),                                             # главная страница
    path('tovar/<str:slug>', views.tovar_show, name='tovar_show'),                   # вывод товара
    path('checkout/<str:slug>', views.checkout, name='checkout'),                    # оформление заказа
    path('tovars/', views.tovars, name='tovars'),                                    # Все товары
    path('tovars/category/<str:slug>', views.tovars_category, name='tovars_category'),        # Показ товаров по категории
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)