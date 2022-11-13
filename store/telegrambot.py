from telebot.async_telebot import AsyncTeleBot
from telebot import types
import django, os, asyncio, math
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()
from django.core.management.base import BaseCommand
from dborm import *
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


bot = AsyncTeleBot('5619487724:AAFeBptlX1aJ9IEAFLMUXN3JZBImJ35quWk')   
product = name(get_products_id())
pages = math.ceil(count_id()/10)
page = 1
first_product = 0
last_product = 10
editing_message = []


@bot.message_handler(commands=['start']) 
async def start(message):
    
    delete_product()
    markut_products = types.ReplyKeyboardMarkup(resize_keyboard=True)
    products = types.KeyboardButton('Products')
    markut_products.add(products)
    await bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}', reply_markup=markut_products)
    


@bot.message_handler(content_types=['text'])
async def text(message):

    delete_product()
    if message.text == 'Products' and "status" not in editing_message:
        list_products = types.InlineKeyboardMarkup(row_width=5)
        for i in range(0, 10):
            list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
        list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='next_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='back_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
        editing_message.append("status")
        await bot.send_message(message.chat.id, f"Products page {page}", reply_markup=list_products)
    
    elif message.text:
        await bot.delete_message(message.chat.id, message.id)
    
         
@bot.callback_query_handler(func=lambda call: True)
async def callback_worker(call):
    global page, pages, first_product, last_product
    for a in range(len(product)):
        if call.data == product[a]:
            description_image_change = description_image_name_price(get_products_id())
            for i in range(len(description_image_change)):
                if product[a] == description_image_change[i][1]:
                    markut_back = types.InlineKeyboardMarkup()
                    back = types.InlineKeyboardButton('Back', callback_data="back")
                    markut_back.add(back)
                    await bot.send_photo(call.message.chat.id, open(description_image_change[i][0], 'rb'))
                    await bot.send_message(call.message.chat.id, f"{description_image_change[i][1]}\n{description_image_change[i][2]}\n{description_image_change[i][3]}", reply_markup=markut_back)
    
    
    if call.data == "back":
        await bot.delete_message(call.message.chat.id, call.message.id)
        await bot.delete_message(call.message.chat.id, call.message.id-1)
        
        
    elif call.data == "first_page" and page != 1:
        page = 1    
        list_products = types.InlineKeyboardMarkup(row_width=5)
        for i in range(0, 10):
            list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
        list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
    
    elif call.data == "next_page" and page != pages:
        if page < pages:
            
            page = page+1
            if page == 2:
                first_product = 10
                last_product = 20
                list_products = types.InlineKeyboardMarkup(row_width=5)
                for i in range(first_product, last_product):

                    list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
                list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
            
            elif page == pages:
                count_last_prod = str(count_id()/10)
                print(count_last_prod)
                index = count_last_prod.find(".")
                count_last_prod = count_last_prod[index+1:]
                print(count_last_prod)
                if count_last_prod == '0':
                    count_last_prod = 10
                list_products = types.InlineKeyboardMarkup(row_width=5)
                for i in range(count_id()-int(count_last_prod), count_id()):
                    list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
                list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
                
            else:
                first_product = first_product+10
                last_product = last_product+10
            
                
                print("a = ", page, first_product, last_product)
                list_products = types.InlineKeyboardMarkup(row_width=5)
                for i in range(first_product, last_product):

                    list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
                list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)

    elif call.data == "back_page" and page != 1:
        if page > 1:
            
            page = page-1
            count_last_prod = str(count_id()/10)
            index = count_last_prod.find(".")
            count_last_prod = count_last_prod[index+1:]
            if count_last_prod == '0':
                count_last_prod = 10
                
            if page == pages-1:
                first_product = count_id()-int(count_last_prod)-10
                last_product = count_id()-int(count_last_prod)
                list_products = types.InlineKeyboardMarkup(row_width=5)
                for i in range(first_product, last_product):   
                    list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
                list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
            
            else:
                first_product = first_product-10
                last_product = last_product-10
                print('b = ', page, first_product, last_product)
                list_products = types.InlineKeyboardMarkup(row_width=5)
                for i in range(first_product, last_product):   
                    list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
                list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
    
    elif call.data == "last_page" and page != pages:
        page = pages   
        count_last_prod = str(count_id()/10)
        print(count_last_prod)
        index = count_last_prod.find(".")
        count_last_prod = count_last_prod[index+1:]
        print(count_last_prod)
        if count_last_prod == '0':
            count_last_prod = 10
        list_products = types.InlineKeyboardMarkup(row_width=5)
        for i in range(count_id()-int(count_last_prod), count_id()):
            list_products.add(types.InlineKeyboardButton(text=f'{product[i]}', callback_data=f'{product[i]}'))
        list_products.add(types.InlineKeyboardButton(text=f'<< 1', callback_data='first_page'),types.InlineKeyboardButton(text=f'<', callback_data='back_page'),
                            types.InlineKeyboardButton(text=f'{page}/{pages}', callback_data=' '),
                            types.InlineKeyboardButton(text=f'>', callback_data='next_page'),types.InlineKeyboardButton(text=f'{pages} >>', callback_data='last_page'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Products page {page}", reply_markup=list_products)
asyncio.run(bot.polling()) 