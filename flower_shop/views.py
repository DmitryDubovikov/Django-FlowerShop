from django.shortcuts import render

from .models import Bouquet


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    context = {"bouquets": Bouquet.objects.all()}
    return render(request, "flower_shop/catalog.html", context)


def quiz(request):
    return render(request, "flower_shop/quiz.html")


def order(request):
    return render(request, "flower_shop/order.html")


def card(request, id):
    try:
        bouquet = Bouquet.objects.get(id=id)
    except Bouquet.DoesNotExist:
        bouquet = None
    context = {
        "bouquet": bouquet,
    }
    return render(request, "flower_shop/card.html", context)
