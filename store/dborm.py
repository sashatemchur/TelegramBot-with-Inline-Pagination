from loguru import logger
import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()
from django.core.management.base import BaseCommand
from bot.models import InfoProducts

logger.add("bot/bot_logs/bot.log", format="{time} {level} {message}", rotation="10MB", compression="zip")


@logger.catch
def delete_product():
    
    logger.info("The (delete_product) function worked")
    product = InfoProducts.objects.all()
    product.filter(status=0).delete()
    
    
@logger.catch
def get_products_id():
    
    logger.info("The (get_products_id) function worked")
    list_id = []
    products = InfoProducts.objects.filter(status=True)
    products = products.values_list('id', flat=True)
    for i in range(len(products)):
        list_id.append(products[i])
    return list_id


@logger.catch
def name(id):
    
    logger.info("The (name) function worked")
    list_product_name  = []
    for i in range(len(get_products_id())):
        product = InfoProducts.objects.get(id=id[i])
        name = product.product_name
        list_product_name.append(name)
    return list_product_name


@logger.catch
def description_image_name_price(id):
    
    logger.info("The (description_image_name_price) function worked")
    description_image_name_price  = []
    for i in range(len(get_products_id())):
        product = InfoProducts.objects.get(id=id[i])
        descriptionimagename = [str(product.image)]
        descriptionimagename.append(product.product_name)
        descriptionimagename.append(product.price)
        descriptionimagename.append(product.description)
        description_image_name_price.append(descriptionimagename)
    return description_image_name_price


@logger.catch
def count_id():
    
    logger.info("The (count_id) function worked")
    product = InfoProducts.objects.filter(status=True)
    return len(product)

