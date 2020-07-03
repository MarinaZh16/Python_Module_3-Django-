from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'in_stock']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'cost', 'is_deleted']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.Return)
