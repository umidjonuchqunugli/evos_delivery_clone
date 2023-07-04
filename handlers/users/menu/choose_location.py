from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.start import bot_start
from keyboards.default.menu import loc_op, loc_history, categories
from loader import dp, bot
from states.location import Location, MenuEvoS


@dp.message_handler(Text(equals='🍴 Menyu'))
async def select_location_bar(message: types.Message):
    await Location.info.set()
    await message.answer('📍 Geolokatsiyani yuboring yoki yetkazib berish manzilini tanlang', reply_markup=loc_op())


@dp.message_handler(Text(equals='⬅️ Ortga'), state=Location.info)
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await bot_start(message=message)


@dp.message_handler(Text(equals='⬅️ Ortga'), state=Location.history)
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await select_location_bar(message=message)


@dp.message_handler(Text(equals='🗺 Mening manzillarim'), state=Location.info)
async def my_loc(message: types.Message):
    await Location.history.set()
    await message.answer('manzillar mavjud emas', reply_markup=loc_history())


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Location.info)
async def location_check(message: types.ContentType.LOCATION, state: FSMContext):
    await state.finish()
    await bot.send_message( chat_id=message['chat']['id'],text="Bo'limni tanlang", reply_markup=categories())
    await MenuEvoS.category.set()
