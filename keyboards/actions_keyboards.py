from aiogram.types import (
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

rnd_num_updated_callback_data = "rnd_num_updated_callback_data"


def actions_kb(button_title) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=button_title, callback_data=rnd_num_updated_callback_data)
    return builder.as_markup()
