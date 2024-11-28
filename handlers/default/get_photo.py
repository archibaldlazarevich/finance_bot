from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router_get_photo = Router()

@router_get_photo.message(Command('get_photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAANPZ0Rr8glatxaB83gs4dAZ_w0fpp8AAr7nMRtGPyBKW6mDd_xtSTYBAAMCAAN5AAM2BA',
                               caption='Это моряк без зубов')