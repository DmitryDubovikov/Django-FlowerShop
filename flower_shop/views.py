from django.shortcuts import render
from phonenumber_field.validators import ValidationError, validate_international_phonenumber

from .models import Bouquet
from more_itertools import chunked
from .models import Bouquet, Consultation, Order


def index(request):
    return render(request, "flower_shop/index.html")


def catalog(request):
    columns_count = 2
    bouquets = Bouquet.objects.all()
    page_columns = list(chunked(bouquets, columns_count))
    context = {
        "page_columns": page_columns,
    }
    return render(request, "flower_shop/catalog.html", context)


def quiz(request):
    return render(request, "flower_shop/quiz.html")


def quiz_step(request):
    return render(request, "flower_shop/quiz-step.html")


def result(request):
    min_price = 0
    max_price = 0
    occasion = 0
    if request.method == "GET" and "fparam" in request.GET and "sparam" in request.GET:
        occasion = request.GET["fparam"]

    all_bouquets = Bouquet.objects.all()
    bouquets_with_price = all_bouquets.filter(price__gte=min_price).filter(price__lte=max_price)
    if not bouquets_with_price:
        bouquets_with_price = all_bouquets

    bouquet = None
    match occasion:
        case 0:
            bouquet = bouquets_with_price.order_by("price")[-1]
        case 1:
            bouquet = bouquets_with_price.order_by("price")[-1]
        case 2:
            bouquet = bouquets_with_price.order_by("price").first()
        case _:
            bouquet = bouquets_with_price.first()

    context = {
        "bouquet": bouquet,
    }
    return render(request, "flower_shop/result.html", context)


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
            bouquet = Bouquet.objects.get(id=bouquet_id)
            new_order = Order.objects.create(
                bouquet=bouquet,
                name=request.GET["fname"],
                phone=request.GET["tel"],
                address=request.GET["adres"],
                preferred_delivery_time=request.GET["orderTime"],
                total_sum=bouquet.price,
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
    if request.method == "GET" and "tel" in request.GET:
        try:
            validate_international_phonenumber(request.GET["tel"])
            Consultation.objects.create(
                firstname=request.GET["fname"], phonenumber=request.GET["tel"]
            )
            context["consultation_created"] = True
        except ValidationError:
            context["bad_phone"] = True
    return render(request, "flower_shop/consultation.html", context)
