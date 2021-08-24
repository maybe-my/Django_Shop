from django.contrib import admin
from .models import Order, OrderItem, Category, Tovar, Slaider, Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sale', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'sale', 'available']
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
    list_display = ['title', 'sub_title','button_title', 'button_url']
    list_filter = ['id', 'created', 'updated']
admin.site.register(Slaider, SlaidbarAdmin)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['id', 'name']
    list_filter = ['id', 'created', 'updated']

admin.site.register(Contact, ContactAdmin)