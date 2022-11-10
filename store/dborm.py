import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()
from django.core.management.base import BaseCommand
from bot.models import InfoProducts


def delete_product():
    product = InfoProducts.objects.all()
    product.filter(status=0).delete()


def name():
    list_product_name  = []
    for i in range(InfoProducts.objects.count()):
        product = InfoProducts.objects.get(id=(i+1))
        name = product.product_name
        list_product_name.append(name)
    return list_product_name


def description_image_name_price():
    description_image_name_price  = []
    for i in range(InfoProducts.objects.count()):
        product = InfoProducts.objects.get(id=(i+1))
        descriptionimagename = [str(product.image)]
        descriptionimagename.append(product.product_name)
        descriptionimagename.append(product.price)
        descriptionimagename.append(product.description)
        description_image_name_price.append(descriptionimagename)
    return description_image_name_price

def count_id():
    for i in range(InfoProducts.objects.count()):
        product = InfoProducts.objects.get(id=(i+1))
    return product.id
