import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        'Здравствуйте, этот бот предоставляет информацию об офинициальных курсах валю НБРБ,'
        ' и данные по наилучшему обмену валют с сайту myfin.by')


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Nice try!')

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
