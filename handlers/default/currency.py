from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.curr_inline import main as inl_cur_keyboard
from api.site_requests import dollar
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import datetime

class CurSt(StatesGroup):
    curr_number = State()

currency_router = Router()

@currency_router.message(Command('cur_rate'))
async def init_message(message: Message, state: FSMContext):
    await state.set_state(CurSt.curr_number)
    await message.reply('Выберите валюту для получения'
                        ' оффициального курса НБРБ',
                        reply_markup= inl_cur_keyboard)


@currency_router.callback_query(F.data.in_(['431', '451', '456']), CurSt.curr_number)
async def rate(callback: CallbackQuery):
    await callback.answer('')
    answer_request = dollar(callback.data)
    await callback.message.edit_text(
        f'Курс {answer_request["Cur_Abbreviation"]} ({answer_request["Cur_Name"].lower()})'
        f' по состоянию на {datetime.date.today().strftime("%d.%m.%Y")}'
        f' : {answer_request["Cur_OfficialRate"]} бел.р. за {answer_request["Cur_Scale"]} единиц(-у) валюты')
