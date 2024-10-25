from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, i18n
from db import database as db
from states.register import RegisterState

from keyboards.default import language


_ = i18n.gettext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await db.get_user(message.from_user.id)

    if not user:
        await message.answer(
            """Tilni tanlang / Выберите язык 👇""", 
            reply_markup = await language.button()
        )
        await RegisterState.language.set()
    else:
        await message.answer(
            _("Salom foydalanuvchi") + " " + message.from_user.full_name
        )


@dp.message_handler(state=RegisterState.language, text=["🇺🇿 O'zbekcha", "🇷🇺 Русский"])
async def language_handler(message: types.Message, state: FSMContext):
    if message.text == "🇺🇿 O'zbekcha":
        language = 'uz'
        answer = "Siz muvvafaqiyatli ro'yxatdan o'tdingiz"
    else:
        language = 'ru'
        answer = "Вы успешно зарегистрировались"
    
    await message.answer(answer)
    await db.get_user_or_create(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        language=language
    )
