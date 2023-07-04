from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='🍴 Menyu')
    button1 = KeyboardButton(text='🛍 Mening buyurtmalarim')
    button2 = KeyboardButton(text='✍️ Fikr bildirish')
    button0 = KeyboardButton(text='⚙️ Sozlamalar')
    rkm.add(button, button1, button2, button0)
    return rkm


def back_to_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='orqaga')
    rkm.add(button)
    return rkm


def cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='cancel')
    rkm.add(button)
    return rkm


def phone_cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='Telefon raqamni ulashish', request_contact=True)
    button0 = KeyboardButton(text='cancel')
    rkm.add(button, button0)
    return rkm


def loc_op():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text='🗺 Mening manzillarim')
    button1 = KeyboardButton(text='📍 Geolokatsiyani yuboring', request_location=True)
    button0 = KeyboardButton(text='⬅️ Ortga')
    rkm.add(button, button1, button0)
    return rkm


def loc_history():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in range(11):
        rkm.add(KeyboardButton(text=f'{i}'))
    rkm.add(KeyboardButton(text='⬅️ Ortga'))
    return rkm


from loader import product, cart


def categories():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in product.all_data:
        rkm.add(KeyboardButton(text=f"{i}"))
    rkm.add(KeyboardButton(text='⬅️ Ortga'))
    return rkm

def product_menu(category):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in product.all_read(category=category):
        rkm.add(KeyboardButton(text=f"{i}"))
    rkm.add(KeyboardButton(text='⬅️ Ortga'))
    return rkm


def back_from_order():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='⬅️ Ortga')
    rkm.add(button)
    return rkm


# def show_carted(customer_id):
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     for i in cart.cart_for_user(customer_id=customer_id):
#         a = f'{i[1]}'
#         rkm.add(KeyboardButton(text=f"{product.get_one_id(id=a)[0]}"))
#     return rkm


# def show_carted(customer_id):
#
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True)
#     for i in cart.cart_for_user(customer_id=customer_id):
#         text = ''
#         for j in i:
#             text+=f' {j}'
#         rkm.add(KeyboardButton(text=text))
#     return rkm


def show_carted(customer_id):

    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in cart.cart_for_user(customer_id=customer_id):
        a = product.get_one_id(i[1])
        rkm.add(KeyboardButton(text=f"{a[0]} - {a[1]}so'm"))
    rkm.add(KeyboardButton(text='orqaga'))
    return rkm
