from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ParseMode
from keyboards.common_keyboards import (
    actions_markup,
    start_markup,
    help_markup,
    ButtonName,
)
from keyboards.inline_keyboards import info_markup

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    print("command text:", repr(message.text))
    await message.answer(
        f"Hello and welcome <b>{message.from_user.full_name} {message.from_user.id}</b>, ! I'm a bot! Please, send me a message or a sticker",
        parse_mode=ParseMode.HTML,
        reply_markup=start_markup,
    )


@router.message(Command("help", prefix="!,/"))
@router.message(F.text == ButtonName.WHAT_NEXT)
async def handle_help(message: types.Message):
    # help_message = (
    #     "This is a help message\\. *Please*, send me a message ||or a sticker||!"
    # )
    help_message = m.text(
        "This is a help message\\.",
        m.text(
            m.bold("Please send me"),
            " send me a _message_ ~hihihi~",
        ),
        "||or a sticker\\!||",
        sep="\n",
    )
    await message.answer(
        text=help_message,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=help_markup,
    )


@router.message(Command("more", prefix="!,/"))
async def handle_more(message: types.Message):
    await message.answer(
        text="Choose action",
        reply_markup=actions_markup,
    )


@router.message(Command("info", prefix="!,/"))
async def handle_info(message: types.Message):
    await message.answer(
        text="Links and another resources",
        reply_markup=info_markup,
    )
