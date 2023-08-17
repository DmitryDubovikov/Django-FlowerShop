from django.shortcuts import render

from .models import Bouquet, Consultation
from phonenumber_field.validators import validate_international_phonenumber, ValidationError


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
