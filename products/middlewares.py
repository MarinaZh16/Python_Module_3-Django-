from django.contrib import messages
from datetime import datetime
from products import models


class CanReturn:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            purchases = models.Purchase.objects.filter(user=request.user)
            for p in purchases:
                term = datetime.timestamp(datetime.now()) - datetime.timestamp(p.created_at)
                if term > 180 and p.status == 1:
                    p.status = p.SUCCESS
                    p.save()
        response = self.get_response(request)
        return response

