from django.shortcuts import render, redirect
from phonenumber_field.validators import ValidationError, validate_international_phonenumber

from more_itertools import chunked
from .models import Bouquet, Consultation, Order, Occasion, Budget
from .payments import send_payment
from .flowers_bot import send_message_to_bot


def index(request):
    bouquets = Bouquet.objects.filter(is_recommended=True)[:3]
    context = {
        "bouquets": bouquets,
    }
    return render(request, "flower_shop/index.html", context)


def catalog(request):
    columns_count = 2
    bouquets = Bouquet.objects.all()
    page_columns = list(chunked(bouquets, columns_count))
    context = {
        "page_columns": page_columns,
    }
    return render(request, "flower_shop/catalog.html", context)


def quiz(request):
    context = {"occasions": Occasion.objects.all()}
    return render(request, "flower_shop/quiz.html", context)


def quiz_step(request):
    context = {"budgets": Budget.objects.all().order_by("-does_metter", "min_price", "max_price")}
    return render(request, "flower_shop/quiz-step.html", context)


def result(request):
    context = {"wrong_parameters": False}
    if (
        request.method == "GET"
        and "occasion" in request.GET
        and "min" in request.GET
        and "max" in request.GET
    ):
        try:
            occasion = request.GET["occasion"]
            min_price = request.GET["min"]
            max_price = request.GET["max"]
            bouquets_with_price = Bouquet.objects.filter(price__gte=min_price).filter(
                price__lte=max_price
            )
            if not bouquets_with_price:
                bouquets_with_price = Bouquet.objects.filter(price__lte=max_price)
            if not bouquets_with_price:
                bouquets_with_price = Bouquet.objects.all()
            target_bouquet = (
                bouquets_with_price.filter(occasions__name=occasion).order_by("-price").first()
            )
            if not target_bouquet:
                target_bouquet = bouquets_with_price.order_by("price").first()
            context["bouquet"] = target_bouquet
        except Exception:
            context["bouquet"] = Bouquet.objects.all().first()
            context["wrong_parameters"] = True
    else:
        context["bouquet"] = Bouquet.objects.all().first()
        context["wrong_parameters"] = True
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
            send_message_to_bot(
                f"Принят новый заказ: {new_order.bouquet}\n телефон {new_order.phone}\n адрес {new_order.address}\n время: {new_order.preferred_delivery_time}"
            )
            create_pay = send_payment(
                new_order.bouquet.price,
                new_order.phone,
                "email@ya.ru",
                new_order.bouquet,
                new_order.pk,
                f"{request.get_host()}/",
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
