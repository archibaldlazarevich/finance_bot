from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=
        [[InlineKeyboardButton(text='Я сегодня его доделаю', callback_data='motivation')],
         [InlineKeyboardButton(text='Я сегодня его точно доделаю', callback_data='motivation'),
          InlineKeyboardButton(text='Точно', callback_data='motivation')],
         ])

cars = ['Я сегодня его доделаю', 'Я сегодня его доделаю', 'Я сегодня его доделаю']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text= car, url='https://www.nbrb.by/apihelp/exrates'))
    return keyboard.adjust(4).as_markup()