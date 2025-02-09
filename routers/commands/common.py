from config import TK
import asyncio
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ChatAction


router = Router(name=__name__)


@router.message()
async def echo(message: types.Message):
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

    # if message.text:
    # await message.answer(text=message.text, entities=message.entities)

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Somehting new has been detected")
    # if message.text:
    #     await message.reply(text=message.text)
    # elif message.sticker:
    #     await message.reply_sticker(sticker=message.sticker.file_id)

    # else:
    #     await message.reply(text="Somehting new has been detected")
