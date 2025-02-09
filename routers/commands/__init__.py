__all__ = ("router",)

from aiogram import Router

from .base_command import router as base_commands_router
from .user_commands import router as user_commands_router
from .common import router as common_router
from .media import router as media_router
from .admin import router as admin_router

router = Router(name=__name__)
router.include_router(admin_router)
router.include_router(base_commands_router)
router.include_router(user_commands_router)
router.include_router(media_router)
# hast to be last
router.include_router(common_router)
