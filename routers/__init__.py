__all__ = ("router",)

from aiogram import Router

from .commands import router as commands_router
from callback_handlers import router as callback_handlers_router

router = Router(name=__name__)
router.include_router(callback_handlers_router)
router.include_router(commands_router)
