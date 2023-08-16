from django.core.validators import MinValueValidator
from django.db import models


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

    class Meta:
        verbose_name = "букет"
        verbose_name_plural = "букеты"

    def __str__(self):
        return self.name
