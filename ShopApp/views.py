from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Category, Tovar, OrderItem, Slaider
from django.shortcuts import get_object_or_404
from .forms import OrderCreateForm

# Create your views here.
def index(request):
    tovars = Tovar.objects.filter(available=True).order_by('-created')[:6]
    categorys = Category.objects.all().order_by('id')[:5]
    slaidbar = Slaider.objects.filter(active=True).order_by('-created')[:3]
    return render(request,
                  'ShopApp/index.html',
                  {'tovars': tovars,
                  'categorys': categorys,
                  'slaidbar': slaidbar,
                  })


def tovars(request):
    tovars = Tovar.objects.filter(available=True).order_by('-created')
    categorys = Category.objects.all()
    top_tovars = Tovar.objects.filter(top=True).filter(available=True).order_by('created')[:3]
    return render(request, 'ShopApp/shop.html', {'tovars': tovars, 'categorys': categorys, 'top_tovars': top_tovars})


def tovars_category(request, slug):
    categorys = Category.objects.all()
    tovars = Tovar.objects.filter(category__slug=slug).filter(available=True)
    top_tovars = Tovar.objects.filter(top=True).filter(available=True).order_by('created')[:3]
    return render(request, 'ShopApp/shop.html', {'tovars': tovars, 'categorys': categorys, 'top_tovars': top_tovars})


def tovar_show(request, slug):
    tovar = get_object_or_404(Tovar,
                                slug=slug,
                                available=True)
    top_tovars = Tovar.objects.filter(top=True).order_by('created')[:6].filter(available=True)
    return render(request, 'ShopApp/detail_product.html', {'tovar': tovar,
                                                            'top_tovars': top_tovars})


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