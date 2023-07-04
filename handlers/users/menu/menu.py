from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.menu.choose_location import select_location_bar
from keyboards.default.menu import categories, product_menu
from loader import dp, product
from states.location import MenuEvoS


@dp.message_handler(state=MenuEvoS.category)
async def choose_menu(message: types.Message, state: FSMContext):
    if message.text == '⬅️ Ortga':
        await select_location_bar(message=message)
    elif message.text in product.all_data:
        await MenuEvoS.product.set()
        await message.answer(text="Bo'limni tanlang", reply_markup=product_menu(category=message.text))
    else:
        await message.answer(text="Bo'limni tanlang", reply_markup=categories())
