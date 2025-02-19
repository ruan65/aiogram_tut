from aiogram import Router

from .actions_callback_handlers import router as actions_router
from .info_callback_handlers import router as info_router
from .shop_callback_handlers import router as shop_router

router = Router(name=__name__)
router.include_router(shop_router)
router.include_router(actions_router)
router.include_router(info_router)
