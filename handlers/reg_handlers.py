from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from config import DB_NAME
from reg_keyboards import kb_request_contact
from reg_states import RegisterStates
from database import Database

reg_router = Router()
db = Database(DB_NAME)


@reg_router.message(F.text == "Ro'yxatdan o'tish")
async def register_start(message: Message, state: FSMContext):
    users = db.get_user(message.from_user.id)
    if users[5]:
        await message.answer(
            f"Hurmatli {users[6]}, siz tizimda ro'yxatdan o'tgansiz!",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "Ro'yxatdan o'tish jarayonini boshlaymiz!\n"
            "Iltimos, to'liq ism familyaingizni kiriting:",
            reply_markup=ReplyKeyboardRemove())
        await state.set_state(RegisterStates.regName)

@reg_router.message(RegisterStates.regName)
async def register_name(message: Message, state=FSMContext):
    await message.answer(
        f"Yaxshi {message.text}\n Iltimos telefon raqamingzni yuboring",
        reply_markup=kb_request_contact)
    await state.update_data(regname=message.text)
    await state.set_state(RegisterStates.regPhone)

@reg_router.message(RegisterStates.regPhone)
async def register_phone(message: Message, state=FSMContext):
    try:
        await state.update_data(regphone=message.contact.phone_number)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')

        await message.answer(
            f"Hurmatli {reg_name}, siz tizimda muvaffaqiyatli ro'yxatdan o'tdingiz",
            reply_markup=ReplyKeyboardRemove())
        db.update_user(message.from_user.id, reg_name, reg_phone)
        await state.clear()
    except:
        await message.answer(
            f"Iltimos, telefon raqamingizni yuboring",
            reply_markup=kb_request_contact)