from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from .actions_keyboards import rnd_num_updated_callback_data

rnd_callback_dice = "rnd_callback_dice"
rnd_callback_modal = "rnd_callback_modal"


def _info_markup() -> InlineKeyboardMarkup:
    tg_channel_button = InlineKeyboardButton(
        text="📣 My Telegram Channel",
        url="https://t.me/mozgo_kluyka",
    )
    tg_chaat_button = InlineKeyboardButton(
        text="💬 Quizarium Telegram Chat",
        url="https://t.me/quizarium",
    )
    btn_random_bot_start = InlineKeyboardButton(
        text="🤖 Random number message",
        callback_data=rnd_num_updated_callback_data,
    )
    btn_random_dice = InlineKeyboardButton(
        text="🎲 Random bot dice",
        callback_data=rnd_callback_dice,
    )

    btn_random_modal = InlineKeyboardButton(
        text="🎲 Show alert",
        callback_data=rnd_callback_modal,
    )
    row1 = [tg_channel_button, tg_chaat_button]
    row2 = [btn_random_bot_start]
    rows = [
        row1,
        row2,
        [btn_random_dice],
        [btn_random_modal],
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


info_markup = _info_markup()
