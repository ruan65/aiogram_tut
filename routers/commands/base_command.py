from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ParseMode

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        f"Hello and welcome <b>{message.from_user.full_name} {message.from_user.id}</b>, ! I'm a bot! Please, send me a message or a sticker",
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help"))
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
    await message.answer(text=help_message, parse_mode=ParseMode.MARKDOWN_V2)
