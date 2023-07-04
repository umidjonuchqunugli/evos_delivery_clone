from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.menu.menu import choose_menu
from keyboards.default.menu import categories, back_from_order
from keyboards.inline.order import add_cart
from loader import dp, product
from states.location import MenuEvoS, Cart


@dp.message_handler(state=MenuEvoS.product)
async def choose_product(message: types.Message, state: FSMContext):
    if message.text == '⬅️ Ortga':
        await MenuEvoS.category.set()
        await message.answer(text="Bo'limni tanlang", reply_markup=categories())
    elif message.text in product.all_get():
        await Cart.order.set()
        async with state.proxy() as data:
            data['product_id'] = product.get_one(f"{message.text}")[2]
        await message.answer('Quyidagilardan birini tanlang', reply_markup=back_from_order())
        await message.answer(text=f'{product.get_one(f"{message.text}")[0]} {product.get_one(f"{message.text}")[1]}',
                             reply_markup=add_cart())
