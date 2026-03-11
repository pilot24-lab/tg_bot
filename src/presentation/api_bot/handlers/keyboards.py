from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

settings_reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='тест')]
])

settings_inline_meal = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить', callback_data='update_meal')],
    [InlineKeyboardButton(text='Удалить', callback_data='delete_meal')]
])