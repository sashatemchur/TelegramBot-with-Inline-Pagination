import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()
from django.core.management.base import BaseCommand
from bot.models import InfoProducts


def delete_product():
    
    product = InfoProducts.objects.all()
    product.filter(status=0).delete()
    
    
def get_products_id():
    
    list_id = []
    products = InfoProducts.objects.filter(status=True)
    products = products.values_list('id', flat=True)
    for i in range(len(products)):
        list_id.append(products[i])
    return list_id

def name(id):
    
    list_product_name  = []
    for i in range(len(get_products_id())):
        product = InfoProducts.objects.get(id=id[i])
        name = product.product_name
        list_product_name.append(name)
    return list_product_name


def description_image_name_price(id):
    
    description_image_name_price  = []
    for i in range(len(get_products_id())):
        product = InfoProducts.objects.get(id=id[i])
        descriptionimagename = [str(product.image)]
        descriptionimagename.append(product.product_name)
        descriptionimagename.append(product.price)
        descriptionimagename.append(product.description)
        description_image_name_price.append(descriptionimagename)
    return description_image_name_price


def count_id():
    
    product = InfoProducts.objects.filter(status=True)
    return len(product)
