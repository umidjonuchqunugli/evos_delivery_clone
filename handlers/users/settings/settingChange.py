from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import bot_start
from keyboards.default.menu import back_to_menu, categories
from loader import dp


@dp.message_handler(Text(equals='⚙️ Sozlamalar'))
async def settings(message: types.Message):
    await message.answer("Sozlamalar vaqtincha o'chirilgan", reply_markup=back_to_menu())

@dp.message_handler(Text(equals='orqaga'))
async def back(message: types.Message):
    await bot_start(message=message)
