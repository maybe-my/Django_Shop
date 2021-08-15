from django.contrib import admin
from .models import Order, OrderItem, Category, Tovar, Slaider, Sub_Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['parent_category']
admin.site.register(Sub_Category, Sub_CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Tovar, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'city', 'paid', ]
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid']
    inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)


class SlaidbarAdmin(admin.ModelAdmin):
    model = Slaider
    list_display = ['id', 'title', 'button_title', 'button_url']
    list_editable = ['title', 'button_title', 'button_url']
    list_filter = ['id', 'created', 'updated']

admin.site.register(Slaider, SlaidbarAdmin)