from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_help = Router()

@router_help.message(Command('help'))
async def get_help(message:Message):
    await message.answer('Это команда help')