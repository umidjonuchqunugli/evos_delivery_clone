from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import bot_start
from keyboards.default.menu import show_carted
from loader import dp


@dp.message_handler(Text(equals='🛍 Mening buyurtmalarim'))
async def showit(message: types.Message):
    await message.answer('Savatingiz:',
                         reply_markup=show_carted(customer_id=f'{message.chat.id}'))

@dp.message_handler(Text(equals='orqaga'))
async def mainmenu(message: types.Message):
    await bot_start(message=message)