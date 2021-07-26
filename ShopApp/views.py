from django.shortcuts import render
from django.http import HttpResponse
from .models import Tovar, OrderItem
from django.shortcuts import get_object_or_404
from .forms import OrderCreateForm

# Create your views here.
def index(request):
    tovars = Tovar.objects.filter(available=True).order_by('-created')[:6]

    return render(request,
                  'ShopApp/index.html',
                  {'tovars': tovars})


def tovar_show(request, slug):
    tovar = get_object_or_404(Tovar,
                                slug=slug,
                                available=True)
    return render(request, 'ShopApp/detail_product.html', {'tovar': tovar})

def checkout(request, slug):
    tovar = get_object_or_404(Tovar, slug=slug, available=True)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            OrderItem.objects.create(order=order, product=tovar,price=tovar.price)
            return HttpResponse('Успешно отправили')
    else:
        form = OrderCreateForm
    return render(request, 'ShopApp/checkout.html', {'tovar': tovar, 'form': form})