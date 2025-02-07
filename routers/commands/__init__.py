__all__ = ("router",)

from aiogram import Router

from .base_command import router as base_commands_router

router = Router()
router.include_router(base_command.router)
