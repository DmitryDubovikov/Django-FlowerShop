from django.contrib import admin

from .models import Bouquet, Order, Consultation, Flower, FlowerSet, Occasion, Budget

admin.site.register(Bouquet)
admin.site.register(Order)
admin.site.register(Consultation)
admin.site.register(Flower)
admin.site.register(FlowerSet)
admin.site.register(Occasion)
admin.site.register(Budget)
