from re import Match
from magic_filter import RegexpMode
from config import settings
from aiogram import Router, types, F


router = Router(name=__name__)


@router.message(F.from_user.id.in_(settings.admin_ids), F.text == "secret")
# @router.message(F.from_user.id.in_([134825803]))
async def admin_message(message: types.Message):
    await message.reply(
        "You are admin",
    )


@router.message(
    F.from_user.id.in_(settings.admin_ids),
    F.text.regexp(r"(\d+)", mode=RegexpMode.MATCH).as_("code"),
)
async def handle_code(message: types.Message, code: Match[str]):
    await message.reply(f"Your code: {code.group()}")
