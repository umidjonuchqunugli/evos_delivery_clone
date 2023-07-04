from aiogram.dispatcher.filters.state import StatesGroup, State


class CustomerReview(StatesGroup):
    customerPhone = State()
    customerText = State()
