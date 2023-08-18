from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Consultation(models.Model):
    firstname = models.CharField("имя", max_length=100)
    phonenumber = PhoneNumberField(
        verbose_name="номер телефона",
        unique=False,
    )

    class Meta:
        verbose_name = "консультация"
        verbose_name_plural = "консультации"

    def __str__(self):
        return f"{self.firstname}: {self.phonenumber.as_e164}"


class Flower(models.Model):
    name = models.CharField("название", max_length=100)
    price = models.DecimalField(
        verbose_name="цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
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
        validators=[MinValueValidator(1)],
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

    def consits_of(self):
        return ", ".join([flover_set.__str__() for flover_set in self.flowers_sets.all()])

    def __str__(self):
        return self.name


class Order(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name="букет")
    name = models.CharField("имя", max_length=100)
    phone = PhoneNumberField(
        verbose_name="номер телефона",
        unique=False,
    )
    address = models.CharField(
        "адрес",
        max_length=100,
        blank=True,
    )
    preferred_delivery_time = models.CharField("желаемое время доставки", max_length=50)
    total_sum = models.DecimalField(
        "сумма", max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"{self.bouquet.name} для {self.name}"
