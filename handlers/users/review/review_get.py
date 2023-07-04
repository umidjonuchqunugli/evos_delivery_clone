from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.start import bot_start
from keyboards.default.menu import menu, cancel, phone_cancel
from loader import dp, review
from states.reviewState import CustomerReview


@dp.message_handler(Text(equals='cancel'), state=CustomerReview)
async def cancel_in(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Fikr bildirish bekor qilindi')
    await bot_start(message=message)


@dp.message_handler(Text(equals='✍️ Fikr bildirish'))
async def start(message: types.Message):
    await CustomerReview.customerPhone.set()
    await message.answer('Telefon raqamingizni kiriting:', reply_markup=phone_cancel())


@dp.message_handler(state=CustomerReview.customerPhone, content_types=types.ContentType.TEXT)
async def phone(message: types.Message):
    await CustomerReview.customerText.set()
    await message.answer('Fikringizni kiriting:', reply_markup=cancel())


@dp.message_handler(state=CustomerReview.customerPhone, content_types=types.ContentType.CONTACT)
async def phone(message: types.ContentType.CONTACT, state: FSMContext):
    await CustomerReview.customerText.set()
    async with state.proxy() as data:
        data['user_id'] = message['from']['id']
        data['phone_number'] = message['contact']['phone_number']
        data['full_name'] = f"{message['from']['first_name']} {message['from']['last_name']}"
        data['username'] = message['from']['username']

    await message.answer('Fikringizni kiriting:', reply_markup=cancel())


@dp.message_handler(state=CustomerReview.customerText)
async def text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['review'] = message['text']
    review.add_review(user_id=data['user_id'],
                      phone_number=data['phone_number'],
                      full_name=data['full_name'],
                      username=data['username'],
                      review=data['review'])
    await message.answer("Fikringiz jo'natildi")
    await state.finish()
    await message.answer('Quyidagilardan birini tanlang:', reply_markup=menu())
