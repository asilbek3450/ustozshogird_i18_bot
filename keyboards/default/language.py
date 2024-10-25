from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def button():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton("🇺🇿 O'zbekcha"),
                KeyboardButton("🇷🇺 Русский")
            ]
        ]
    )