from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Category, Tovar, OrderItem, Slaider
from django.shortcuts import get_object_or_404
from .forms import OrderCreateForm, ContactCreateForm
import requests

# Create your views here.
def index(request):
    tovar_top_one = Tovar.objects.filter(available=True, top=True).order_by('-created')[:1]
    tovar_top = Tovar.objects.filter(available=True, top=True).order_by('-created')[:8]
    tovars_all = Tovar.objects.filter(available=True).order_by('-created')[:8]
    tovars_new = Tovar.objects.filter(available=True, new=True).order_by('-created')[:8]
    tovars_women = Tovar.objects.filter(available=True, family='w').order_by('-created')[:8]
    tovars_man = Tovar.objects.filter(available=True, family='m').order_by('-created')[:8]
    tovars_kids = Tovar.objects.filter(available=True, family='k').order_by('-created')[:8]
    categorys = Category.objects.all().order_by('id')[:5]
    slaidbar = Slaider.objects.filter(active=True).order_by('-created')[:3]
    return render(request,
                  'ShopApp/index.html',
                    {
                    'categorys': categorys,
                    'slaidbar': slaidbar,
                    'tovars_all': tovars_all,
                    'tovars_new': tovars_new,
                    'tovar_top': tovar_top,
                    'tovars_women': tovars_women,
                    'tovars_man': tovars_man,
                    'tovars_kids': tovars_kids,
                    'tovar_top_one': tovar_top_one,
                    })


def tovars(request, size=''):
    tovars = get_size(size)
    tovars_all = tovars
    categorys = Category.objects.all()
    top_tovars = Tovar.objects.filter(top=True, available=True).order_by('created')[:3]
    return render(request, 'ShopApp/shop_filter.html', {'tovars': tovars, 'categorys': categorys, 'top_tovars': top_tovars, 'tovars_all': tovars_all})


def tovars_category(request, slug):
    tovars= Tovar.objects.filter(category__slug=slug).filter(available=True)
    categorys = Category.objects.all()
    tovars_all = Tovar.objects.filter(available=True).order_by('-created')
    top_tovars = Tovar.objects.filter(top=True).filter(available=True).order_by('created')[:3]
    # Filter Size
    M = Tovar.objects.filter(available=True, M=True).order_by('-created')
    return render(request, 'ShopApp/shop_filter.html', {'tovars': tovars, 
                                                        'categorys': categorys, 
                                                        'top_tovars': top_tovars, 
                                                        'tovars_all': tovars_all,})


def tovar_show(request, slug):
    tovar = get_object_or_404(Tovar,
                                slug=slug,
                                available=True)
    top_tovars = Tovar.objects.filter(top=True, available=True).order_by('created')[:8]
    return render(request, 'ShopApp/detail_product.html', {'tovar': tovar,
                                                            'top_tovars': top_tovars})


def checkout(request, slug):
    tovar = get_object_or_404(Tovar, slug=slug, available=True)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            OrderItem.objects.create(order=order, product=tovar,price=tovar.get_sale())

            message = \
            f""" ?????????? ?????????? ???{order.id}!
        ????????????: {order.first_name} {order.last_name}, ???? {order.city} ({order.address}) ??????????????(??) - {tovar.name} ???? ?????????? - {tovar.get_sale()} ??????!
        ????????????????: Email: {order.email}. ??????????????: {order.phone}.
        ??????????????: {order.paid}. 
        ???????????????????? ?? ????????????: {order.comment}.

        ???????????????????? --> http://127.0.0.1:8000/admin/ShopApp/order/{order.id}/change
            """
            requests.get("https://api.telegram.org/bot1871010669:AAG7fYv8N9t3L2_tGLL4TknGoLTpqmcK9lo/sendMessage?chat_id=403686785&text=" + message)
            return redirect('/')
    else:
        form = OrderCreateForm
    return render(request, 'ShopApp/checkout.html', {'tovar': tovar, 'form': form})


def express(request):
    return render(request, 'ShopApp/express.html')


def contact(request):
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactCreateForm
    return render(request, 'ShopApp/contact.html', {'form': form})


# Functions

def get_size(size):
    if size == 'S':
        tovars = Tovar.objects.filter(available=True, S=True).order_by('-created')
    elif size == 'M':
        tovars = Tovar.objects.filter(available=True, M=True).order_by('-created')
    elif size == 'L':
        tovars = Tovar.objects.filter(available=True, L=True).order_by('-created')
    elif size == 'XL':
        tovars = Tovar.objects.filter(available=True, XL=True).order_by('-created')
    elif size == 'XXL':
        tovars = Tovar.objects.filter(available=True, XXL=True).order_by('-created')
    elif size == 'XXXL':
        tovars = Tovar.objects.filter(available=True, XXXL=True).order_by('-created')
    else:
        tovars = Tovar.objects.filter(available=True).order_by('-created')
    return tovars
