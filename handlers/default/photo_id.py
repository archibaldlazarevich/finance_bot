from aiogram import F, Router
from aiogram.types import Message

router_photo_id = Router()

@router_photo_id.message(F.photo)
async  def get_photo(message:Message):
    await message.answer('ID фото: {}'.format(message.photo[-1].file_id))
