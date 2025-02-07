import csv
import aiohttp
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


@dp.message(Command("code"))
async def handle_code(message: types.Message):
    code = """
    def hello():
        print("Hello, World!")
    """
    text = m.code(
        code,
        "",
        sep="\n",
    )
    await message.answer(text=code)


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


@dp.message(Command("pic"))
async def handle_pic(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    # url = "https://static01.nyt.com/images/2024/03/05/autossell/00TB-MEOWS/00TB-MEOWS-square640.jpg"
    # url = "https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg"
    url = "https://images5.alphacoders.com/130/thumb-1920-1302858.jpg"
    await message.reply_photo(url)


async def send_big_file(message: types.Message):
    await asyncio.sleep(8)
    url = "https://images.unsplash.com/photo-1529778873920-4da4926a72c2?q=80&w=2672&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    file = io.BytesIO()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            bytes_data = await response.read()
    file.write(bytes_data)
    await message.reply_document(
        document=types.BufferedInputFile(
            # file=bytes_data,
            file=file.getvalue(),
            filename="cat-big-photo.jpg",
        )
    )


@dp.message(Command("pic_file"))
async def handle_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    # action_sender = ChatActionSender(
    #     bot=message.bot,
    #     chat_id=message.chat.id,
    #     action=ChatAction.UPLOAD_DOCUMENT,
    # )
    action_sender = ChatActionSender.upload_document(
        bot=message.bot,
        chat_id=message.chat.id,
    )
    async with action_sender:
        await send_big_file(message)


@dp.message(Command("file"))
async def handle_command_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    file_path = "/Users/a/dev/tmp/wallpaperflare.com_wallpaper.jpg"
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="cat-big-photo.jpg",
        ),
    )
    # sent_file_id = sent_message.document.file_id
    # print(sent_file_id)


@dp.message(Command("text"))
async def handle_command_text(message: types.Message):
    file = io.StringIO()
    file.write("Hi bytes\n")
    file.write("Ont more time hi bytes\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="greeting.txt",
        )
    )


@dp.message(Command("csv"))
async def handle_command_csv(message: types.Message):
    file = io.StringIO()
    csv.writer(file).writerow(["first name", "last name", "age", "city"])
    csv.writer(file).writerow(["John", "Smith", "33", "London"])
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="peope.csv",
        )
    )


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
