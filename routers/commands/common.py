import logging
from config import TK
import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ChatAction
from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.fsm.context import FSMContext

from keyboards.common_keyboards import ButtonName


router = Router(name=__name__)


@router.message(F.text == ButtonName.CANCEL)
async def handle_cancel(message: Message):
    await message.answer(
        text="See you later!, Click /start to start again",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("Ok. No state to cancel")
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled state: {current_state}",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message()
async def echo(message: Message):
    if message.poll:
        await message.forward(chat_id=message.chat.id)
        return
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Start processing...",
    )
    await message.bot.send_message(
        chat_id=message.chat.id,
        text=f"sticker detected" if message.sticker else "Detected message",
        reply_to_message_id=message.message_id,
    )

    await message.answer(
        "Wait a second...",
        parse_mode=None,
    )

    if message.sticker:
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.CHOOSE_STICKER,
        )
        await asyncio.sleep(4)

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Somehting new has been detected")
