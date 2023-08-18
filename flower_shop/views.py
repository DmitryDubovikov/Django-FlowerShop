from django.shortcuts import render, redirect, get_object_or_404
from phonenumber_field.validators import (ValidationError,
                                          validate_international_phonenumber)

from .models import Bouquet
from more_itertools import chunked
from .models import Bouquet, Consultation, Order
from datetime import datetime
from .payments import send_payment


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
            create_pay = send_payment(
                new_order.bouquet.price, new_order.phone, 'email@ya.ru', new_order.bouquet, new_order.pk
            )
            url = create_pay["confirmation"]["confirmation_url"]
            return redirect(url)

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





