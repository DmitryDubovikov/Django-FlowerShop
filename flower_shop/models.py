from django.core.validators import MinValueValidator
from django.db import models


class Flower(models.Model):
    name = models.CharField("название", max_length=100)
    price = models.IntegerField(
        verbose_name="цена цветка",
    )

    class Meta:
        verbose_name = "цветок"
        verbose_name_plural = "цветы"

    def __str__(self):
        return self.name


class FlowerSet(models.Model):
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name="flower_set",
        verbose_name="набор цветов",
    )
    count = models.IntegerField(
        verbose_name="число",
    )

    class Meta:
        verbose_name = "набор цветов"
        verbose_name_plural = "наборы цветов"

    def __str__(self):
        return f"{self.flower.name} - {self.count} шт."


class BouquetQuerySet(models.QuerySet):
    def recommended(self):
        return self.filter(is_recommended=True)


class Bouquet(models.Model):
    name = models.CharField("название", max_length=100)
    description = models.TextField(
        "описание",
        max_length=250,
        blank=True,
    )
    is_recommended = models.BooleanField(
        "рекомендуем",
        default=False,
        db_index=True,
    )
    price = models.DecimalField(
        "цена", max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    image = models.ImageField("картинка", upload_to="bouquet_images")

    objects = BouquetQuerySet.as_manager()

    flowers_sets = models.ManyToManyField(
        FlowerSet,
        related_name="bouquet",
        verbose_name="наборы цветов",
    )

    height = models.IntegerField(
        verbose_name="высота",
    )
    width = models.IntegerField(
        verbose_name="ширина",
    )

    class Meta:
        verbose_name = "букет"
        verbose_name_plural = "букеты"

    def __str__(self):
        return self.name
