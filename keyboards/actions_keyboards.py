from random import randint
from aiogram.types import (
    InlineKeyboardMarkup,
)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

rnd_num_updated_callback_data = "rnd_num_updated_callback_data"


class FixedRandomNumCallbackData(CallbackData, prefix="fixed-random-num"):
    number: int


def actions_kb(button_title) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=button_title,
        callback_data=rnd_num_updated_callback_data,
    )
    cb_data_1 = FixedRandomNumCallbackData(number=randint(1, 101))
    builder.button(
        text=f"Random number: {cb_data_1.number}",
        callback_data=cb_data_1.pack(),
    )
    builder.button(
        text="Random number: [HIDDEN]",
        callback_data=FixedRandomNumCallbackData(number=randint(1, 101)).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()
