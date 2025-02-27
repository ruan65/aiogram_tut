from aiogram import Router

from .survey_handlers import router as survey_handlers_router
from .user_email_handlers import router as user_email_handlers_router
from .sport_handlers import router as sport_handlers_router

router = Router(name="survey")
router.include_router(survey_handlers_router)
router.include_router(user_email_handlers_router)
router.include_router(sport_handlers_router)
