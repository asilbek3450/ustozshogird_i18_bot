from typing import Any, Tuple
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from aiogram.types import Message

from db import database as db

class I18nMiddleware(BaseI18nMiddleware):
    async def get_locale(self, message: Message, *args: Any, **kwargs: Any) -> str | None:
        user = await db.get_user(message.from_user.id)

        if user:
            return user[-1]
        else:
            return 'uz'
