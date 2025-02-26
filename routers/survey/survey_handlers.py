import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, any_state
from aiogram import F
from email_validator import EmailNotValidError, validate_email

from keyboards.common_keyboards import build_yes_no_keyboard
from routers.survey.email_validater import (
    valid_email_filter,
    # valid_email_or_none,
    # valid_email,
)
from email_validator import EmailNotValidError, validate_email
from routers.survey.states import Survey

router = Router(name=__name__)


@router.message(
    Command("survey", prefix="!,/"),
    default_state,
)
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(Survey.full_name)
    await message.answer(
        text="Please answer the survey, What is your name?",
    )


@router.message(Command("cancel"), Survey())
@router.message(F.text.casefold() == "cancel", Survey())
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        await message.reply(
            "Ok. No state to cancel. Start survey: /survey",
            reply_markup=ReplyKeyboardRemove(),
        )
        return

    logging.info(f"Cancelling survey on step: {current_state}. Start again: /survey")
    await state.clear()
    await message.answer(
        f"Cancelled state: {current_state}",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Survey.full_name, F.text)
async def handle_user_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(Survey.email)
    await message.answer(
        text=f"Your name is {markdown.hbold(message.text)}\nPlease enter your email",
        reply_markup=ReplyKeyboardRemove(),
    )
