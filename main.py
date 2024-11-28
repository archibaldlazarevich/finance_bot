import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers.default.start import router_start
from handlers.default.get_photo import router_get_photo
from handlers.default.photo_id import router_photo_id
from handlers.default.text_answer import router_answer
from handlers.default.help import router_help
from handlers.default.reg import reg_router
from handlers.default.currency import currency_router

from config.config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        router_answer,
        router_help,
        router_photo_id,
        router_start,
        router_get_photo,
        reg_router,
        currency_router
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')