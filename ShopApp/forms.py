from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        # }
        labels = {
           'first_name': ('Имя'),
           'last_name': ('Фамилия'),
           'email': ('Email'),
        #    'first_name': ('Имя'),
        #    'first_name': ('Имя'),
        #    'first_name': ('Имя'),
       }
        
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'