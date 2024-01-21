from products import models as product_models


def categories(request):
    categories = product_models.Category.objects.filter(
        status=product_models.Category.Status.SHOW
    )
    return {"categories": categories}
