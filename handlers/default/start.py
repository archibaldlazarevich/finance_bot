from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from api.site_requests import dollar
from aiogram.fsm.state import StatesGroup, State
from middlewares import TestMiddleware

import datetime


import keyboards.reply as rep
import keyboards.inline as inl

router_start = Router()

router_start.message.outer_middleware(TestMiddleware())

@router_start.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!\nТвой ID: {}.\nИмя: {}.\nФамилия: {}.'.format(
        message.from_user.id, message.from_user.first_name,
        message.from_user.last_name),
        reply_markup=inl.main)

# @router_start.callback_query(F.data == 'motivation')
# async def motivation(callback: CallbackQuery):
#     await callback.answer('Ваш выбор учтен', show_alert=True)
#     await callback.message.edit_text('Hello!', reply_markup= await inl.inline_cars())


@router_start.callback_query(F.data == 'motivation')
async def motivation(callback: CallbackQuery):
    await callback.message.reply(f'Курс доллара на {datetime.date.today()}:'
                                 f' {dollar()}')


