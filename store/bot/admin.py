from django.contrib import admin
from bot.models import InfoProducts
from faker import Faker






@admin.register(InfoProducts)
class InfoProductsAdmin(admin.ModelAdmin):
    
    list_display = ('product_name', 'description', 'price', 'image', 'status')
    list_filter = ('product_name', 'description', 'price', 'image', 'status')
    search_fields = ('product_name', 'description', 'price', 'image', 'status')
    
    '''
    faker = Faker('en_US')
    for _ in range(500):
        id = _
        full_name = faker.name()
        email = faker.text()
        phone = faker.random.randint(5000, 15000)
        address = 'png'
        balance = 1
        data = InfoProducts(id = id, product_name = full_name, description = email, price = phone, image = address, status = balance)
        data.save()'''