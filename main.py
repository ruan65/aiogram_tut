from ast import parse

from aiogram.client.bot import DefaultBotProperties
from config import TK
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from routers import router as main_router


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
        token=TK,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
