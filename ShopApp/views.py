from django.shortcuts import render
from .models import Tovar

# Create your views here.
def index(request):
    tovars = Tovar.objects.filter(available=True)

    return render(request,
                  'ShopApp/index.html',
                  {'tovars': tovars})


def tovar_show(request):
    tovars = Tovar.objects.filter(available=True)
    return render(request,
                  'ShopApp/index.html',
                  {'tovars': tovars})