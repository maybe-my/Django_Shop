from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'comment']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        # }
        labels = {
           'first_name': ('Имя'),
           'last_name': ('Фамилия'),
           'email': ('Email'),
           'phone': ('Номер телефона'),
           'address': ('Адресс'),
           'city': ('Город'),
           'comment': ('Коментарий к заказу')
       }
        
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'