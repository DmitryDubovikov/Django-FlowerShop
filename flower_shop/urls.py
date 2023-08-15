from django.urls import path
from .views import index

app_name = "flower_shop"

urlpatterns = [
    path("", index, name="index"),
]
