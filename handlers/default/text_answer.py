from aiogram import F, Router
from aiogram.types import Message

router_answer = Router()

@router_answer.message(F.text == 'Как дела')
async def get_deals(message:Message):
    await message.answer('Все хорошо!!')