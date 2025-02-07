import csv
import aiohttp
import io
import asyncio
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown as m
from aiogram.enums import ParseMode
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.chat_action import ChatActionSender

router = Router(name=__name__)


@router.message(Command("code"))
async def handle_code(message: types.Message):
    code = """
    def hello():
        print("Hi my dear friends!")
    """
    text = m.code(
        code,
        "",
        sep="\n",
    )
    await message.answer(text=code)


@router.message(Command("pic"))
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


@router.message(Command("pic_file"))
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


@router.message(Command("file"))
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


@router.message(Command("text"))
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


@router.message(Command("csv"))
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
