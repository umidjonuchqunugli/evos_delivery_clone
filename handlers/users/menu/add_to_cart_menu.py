from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import categories
from loader import dp, cart
from states.location import Cart, MenuEvoS


@dp.callback_query_handler(state=Cart.order)
async def order(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'savatga':
        async with state.proxy() as data:
            product_id = data['product_id']
        cart.add_to_cart(product_id=product_id,
                         customer_id=callback.message.chat.id)
        await callback.answer('Added')


@dp.message_handler(state=Cart.order)
async def back(message: types.Message):
    if message.text == '⬅️ Ortga':
        await MenuEvoS.category.set()
        await message.answer(text='Tanlang', reply_markup=categories())