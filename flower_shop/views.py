from django.shortcuts import render
from phonenumber_field.validators import (ValidationError,
                                          validate_international_phonenumber)

from .models import Bouquet, Consultation, Order


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    context = {"bouquets": Bouquet.objects.all()}
    return render(request, "flower_shop/catalog.html", context)


def quiz(request):
    return render(request, "flower_shop/quiz.html")


def order(request, bouquet_id):
    if len(request.GET) == 0:
        # render order.html
        context = {"bouquet_id": bouquet_id}
        return render(request, "flower_shop/order.html", context)

    # create order and render order-step.html
    context = {}
    if request.method == "GET":
        try:
            validate_international_phonenumber(request.GET["tel"])
            new_order = Order.objects.create(
                bouquet=Bouquet.objects.get(id=bouquet_id),
                name=request.GET["fname"],
                phone=request.GET["tel"],
                address=request.GET["adres"],
                preferred_delivery_time=request.GET["orderTime"],
            )
            context["order_created"] = True
            context["order_id"] = new_order.id
            return render(request, "flower_shop/order-step.html", context)
        except ValidationError:
            context["order_created"] = False
            return render(request, "flower_shop/order.html", {"bouquet_id": bouquet_id})


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
    context = {
        "bad_phone": False,
        "consultation_created": False,
    }
    if request.method == "GET":
        try:
            validate_international_phonenumber(request.GET["tel"])
            Consultation.objects.create(
                firstname=request.GET["fname"], phonenumber=request.GET["tel"]
            )
            context["consultation_created"] = True
        except ValidationError:
            context["bad_phone"] = True
    return render(request, "flower_shop/consultation.html", context)
