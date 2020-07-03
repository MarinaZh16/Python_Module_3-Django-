from django.db import models
from django.conf import settings


USER_MODEL = settings.AUTH_USER_MODEL


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Product(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True, verbose_name='Цена, $')
    in_stock = models.BooleanField(default=False, db_index=True, verbose_name='В наличии')
    quantity = models.IntegerField(default=0, verbose_name='Кол-во на складе')
    image = models.ImageField(blank=True, null=True, upload_to='media/product_images/')

    def save(self, *args, **kwargs):
        if self.quantity > 0:
            self.in_stock = True
        elif self.quantity <= 0:
            self.in_stock = False
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Purchase(TimestampModel):
    NEW = 1
    IN_PROCESSING = 2
    DECLINED = 3
    APPROVED = 4
    SUCCESS = 5

    STATUSES = (
        (NEW, 'NEW'),
        (IN_PROCESSING, 'IN_PROCESSING'),
        (DECLINED, 'CANCELLATION_DECLINED'),
        (APPROVED, 'APPROVED'),
        (SUCCESS, 'SUCCESS'),
    )

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    cost = models.FloatField(default=0)
    status = models.PositiveSmallIntegerField(default=NEW, choices=STATUSES)

    def save(self, *args, **kwargs):
        super(Purchase, self).save(*args, **kwargs)

    def __str__(self):
        return f"Product:{self.product} {self.cost}"


class Return(TimestampModel):
    NEW = 1
    DECLINED = 2
    APPROVED = 3

    STATUSES = (
        (NEW, 'NEW'),
        (DECLINED, 'DECLINED'),
        (APPROVED, 'APPROVED'),
    )
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=True, null=True)
    cancelled = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=NEW, choices=STATUSES)

    def save(self, *args, **kwargs):
        super(Return, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.purchase.product} {self.purchase.cost}"