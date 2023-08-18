from django.shortcuts import render

from .models import Bouquet
from more_itertools import chunked


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    columns_count = 2
    bouquets = Bouquet.objects.all()
    page_columns = list(chunked(bouquets, columns_count))
    context = {
        'page_columns': page_columns,
    }
    return render(request, "flower_shop/catalog.html", context)


def card(request, id):
    try:
        bouquet = Bouquet.objects.get(id=id)
    except Bouquet.DoesNotExist:
        bouquet = None
    context = {
        "bouquet": bouquet,
    }
    return render(request, "flower_shop/card.html", context)
