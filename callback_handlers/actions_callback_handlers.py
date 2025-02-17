from random import randint
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.actions_keyboards import (
    actions_kb,
    rnd_num_updated_callback_data,
)

router = Router(name=__name__)


@router.callback_query(F.data == rnd_num_updated_callback_data)
async def handle_random_number_edited(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=f"Your random number: {randint(1, 101)}",
        reply_markup=actions_kb("generate"),
    )
