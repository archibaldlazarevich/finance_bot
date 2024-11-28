from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=
    [[InlineKeyboardButton(text='USD', callback_data='431')],
     [InlineKeyboardButton(text='EUR', callback_data='451')],
     [InlineKeyboardButton(text='RUB', callback_data='456')]
    ]
)