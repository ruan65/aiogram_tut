from config import TK
import asyncio
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ChatAction


router = Router(name=__name__)


@router.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    caption = f"Photo detected, description: {message.caption}"
    # message.photo
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


@router.message(F.photo)
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


@router.message(any_media_filter, ~F.caption)
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
