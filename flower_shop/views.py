from django.shortcuts import render

from .models import Bouquet


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    context = {"bouquets": Bouquet.objects.all()}
    return render(request, "flower_shop/catalog.html", context)


def quiz(request):
    return render(request, "flower_shop/quiz.html")


def order(request, bouquet_id):
    context = {"bouquet_id": bouquet_id}
    return render(request, "flower_shop/order.html", context)


def card(request, bouquet_id):
    try:
        bouquet = Bouquet.objects.get(id=bouquet_id)
    except Bouquet.DoesNotExist:
        bouquet = None
    context = {
        "bouquet": bouquet,
    }
    return render(request, "flower_shop/card.html", context)


def consultation(request):
    return render(request, "flower_shop/consultation.html")
