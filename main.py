from config import TK
import asyncio
import logging
from aiogram import Bot, Dispatcher
from routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


async def main():
    bot = Bot(token=TK)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
