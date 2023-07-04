from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_cart():
    rkm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Savatga", callback_data='savatga')
    rkm.add(button)
    return rkm