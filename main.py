from config import TK
import io
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.chat_action import ChatActionSender
from routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


# @dp.message(F.photo, ~F.caption)
# async def handle_photo_wo_caption(message: types.Message):
#     caption = f"Photo detected, description: {message.caption}"
#     # message.photo
#     await message.reply_photo(
#         photo=message.photo[-1].file_id,
#         caption=caption,
#     )


@dp.message(F.photo)
async def handle_photo_wo_caption(message: types.Message):
    caption = f"Photo detected, description: {message.caption}"
    # message.photo
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


any_media_filter = (
    F.photo
    | F.video
    | F.audio
    | F.voice
    | F.video_note
    | F.document
    | F.animation
    # | F.sticker
)


@dp.message(any_media_filter, ~F.caption)
async def handle_any_media_without_caption(message: types.Message):
    if message.document:
        await message.reply_document(
            document=message.document.file_id,
            caption=f"I have got document: {message.document.file_id}",
        )
    elif message.video:
        await message.reply_video(video=message.video.file_id)
    else:
        await message.reply("I cant't see.....")


# @dp.message()
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


async def main():
    bot = Bot(token=TK)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
