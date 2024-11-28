from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'),KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,
    input_field_placeholder='Выбурите пункт меню'
)

cars = ['asads', 'as123wqesd','asdasdasd']

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text= car))
    return keyboard.adjust(2).as_markup()