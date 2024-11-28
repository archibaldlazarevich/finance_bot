from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

reg_router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@reg_router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите Ваше имя')

@reg_router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона')


@reg_router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена.\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()