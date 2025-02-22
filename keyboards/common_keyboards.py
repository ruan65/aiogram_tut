from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonName:
    HELLO = "Hello"
    WHAT_NEXT = "What next?"
    CANCEL = "Cancel"


def _start_markup():
    button_send = KeyboardButton(text=ButtonName.HELLO)
    button_help = KeyboardButton(text=ButtonName.WHAT_NEXT)
    button_cancel = KeyboardButton(text=ButtonName.CANCEL)
    row1 = [button_send]
    row2 = [button_help, button_cancel]
    return ReplyKeyboardMarkup(
        keyboard=[row1, row2],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def list_of_numbers(first: int, last: int):
    return [str(i) for i in range(first, last + 1, 1)]


def buttons_row(names: list[str]):
    return [KeyboardButton(text=name) for name in names]


def _help_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for num in list_of_numbers(1, 10):
        builder.button(text=num)

    builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)


def _actions_markup() -> ReplyKeyboardMarkup:
    # markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    #     [

    #     ]
    # ],)
    # return markup
    builder = ReplyKeyboardBuilder()
    builder.button(text="🌍 Send location", request_location=True)
    builder.button(text="☎️ Send phone", request_contact=True)
    builder.button(text="📊 Send poll", request_poll=KeyboardButtonPollType())
    builder.button(text="🗺️ Send quiz", request_poll=KeyboardButtonPollType(type="quiz"))
    builder.button(
        text="🍔 Dinner?", request_poll=KeyboardButtonPollType(type="reqular")
    )
    builder.button(text=ButtonName.CANCEL)
    builder.adjust(1)
    return builder.as_markup(
        input_field_placeholder="Choose action:", resize_keyboard=True
    )


def build_yes_no_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Yes")
    builder.button(text="No")
    return builder.as_markup(resize_keyboard=True)


start_markup = _start_markup()
help_markup = _help_markup()
actions_markup = _actions_markup()
