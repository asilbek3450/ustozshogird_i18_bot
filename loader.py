from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from middlewares.i18n import I18nMiddleware
from middlewares.throttling import ThrottlingMiddleware

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
i18n = I18nMiddleware(
    domain='messages',
    path='locales/',
    default='uz'
)

i18n.setup(dp)
dp.middleware.setup(ThrottlingMiddleware())