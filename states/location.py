from aiogram.dispatcher.filters.state import StatesGroup, State


class Location(StatesGroup):
    info = State()
    history = State()


class MenuEvoS(StatesGroup):
    category = State()
    product = State()

class Cart(StatesGroup):
    order = State()