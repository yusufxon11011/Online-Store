from aiogram.fsm.state import State, StatesGroup


class CategoryStates(StatesGroup):
    newCategory_state = State()

    updCategory_state_list = State()
    updCategory_state_new = State()

    delCategory_state = State()

class ProductStates(StatesGroup):
    newProduct_state = State()

    updProduct_state_list = State()
    updProduct_state_new = State()

    delProduct_state = State()

class AdStates(StatesGroup):
    newAd_state = State()

    updAd_state_list = State()
    updAd_state_new = State()

    delAd_state = State()
    searchAd_state = State()