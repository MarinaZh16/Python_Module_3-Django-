from products import models


def pending_returns(request):
    new_returns_count = models.Return.objects.filter(status=1).count()
    return {'NEW_RETURNS': new_returns_count}
