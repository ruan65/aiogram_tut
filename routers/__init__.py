__all__ = ("router",)

from aiogram import Router

from callback_handlers import router as callback_handlers_router
from .commands import router as commands_router
from .survey import router as survey_router

router = Router(name=__name__)
router.include_router(survey_router)
router.include_router(callback_handlers_router)
router.include_router(commands_router)
