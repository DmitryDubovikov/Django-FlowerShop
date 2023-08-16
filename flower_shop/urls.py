from django.urls import path

from .views import card, catalog, index, quiz

app_name = "flower_shop"

urlpatterns = [
    path("", index, name="index"),
    path("catalog/", catalog, name="catalog"),
    path("card/<int:id>", card, name="card"),
    path("quiz/", quiz, name="quiz"),
]
