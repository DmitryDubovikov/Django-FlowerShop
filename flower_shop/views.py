from django.shortcuts import render

from .models import Bouquet


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    context = {"bouquets": Bouquet.objects.all()}
    return render(request, "flower_shop/catalog.html", context)
