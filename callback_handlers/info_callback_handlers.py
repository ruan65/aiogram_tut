from random import randint
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards import (
    RandomNumAction,
    RandomNumCallbackData,
)

router = Router(name=__name__)


@router.callback_query(
    RandomNumCallbackData.filter(F.action == RandomNumAction.dice),
)
async def handle_dice(callback_query: CallbackQuery):

    await callback_query.answer(
        text=f"Your random dice: {randint(1, 6)}",
        cache_time=5,
    )


@router.callback_query(
    RandomNumCallbackData.filter(F.action == RandomNumAction.modal),
)
async def handle_modal(callback_query: CallbackQuery):

    await callback_query.answer(
        show_alert=True,
        text=f"Your random dice: {randint(1, 100)}",
        cache_time=5,
    )
