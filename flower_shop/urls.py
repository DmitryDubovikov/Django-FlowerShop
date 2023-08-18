from django.urls import path

from .views import card, catalog, consultation, index, order, quiz, quiz_step, result

app_name = "flower_shop"

urlpatterns = [
    path("", index, name="index"),
    path("catalog/", catalog, name="catalog"),
    path("card/<int:bouquet_id>", card, name="card"),
    path("quiz/", quiz, name="quiz"),
    path("quiz-step/", quiz_step, name="quiz-step"),
    path("result/", result, name="result"),
    path("order/<int:bouquet_id>", order, name="order"),
    path("consultation/", consultation, name="consultation"),
]
