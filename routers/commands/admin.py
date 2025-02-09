from config import settings
from aiogram import Router, types, F


router = Router(name=__name__)


@router.message(F.from_user.id.in_(settings.admin_ids), F.text == "secret")
# @router.message(F.from_user.id.in_([134825803]))
async def admin_message(message: types.Message):
    await message.reply(
        "You are admin",
    )
