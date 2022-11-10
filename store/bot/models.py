from django.db import models


class InfoProducts(models.Model):
    product_name = models.CharField('Product Name', max_length=250)
    description = models.TextField('Descroption', max_length=250)
    price = models.FloatField('Price', max_length=250)
    image = models.ImageField('Image', max_length=250)
    status = models.BooleanField('Status')  
      
    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товари"