from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext
from magic_filter import F

from routers.survey.email_validater import valid_email_filter
from routers.survey.states import Survey

router = Router(name=__name__)


@router.message(Command("survey", prefix="!,/"))
@router.message(Command("survey", prefix="!,/"))
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(Survey.full_name)
    await message.answer(
        text="Please answer the survey, What is your name?",
    )


@router.message(Survey.full_name, F.text)
async def handle_user_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(Survey.email)
    await message.answer(
        text=f"Your name is {markdown.hbold(message.text)}\nPlease enter your email",
    )


@router.message(Survey.email, valid_email_filter)
async def handle_user_email(
    message: Message,
    state: FSMContext,
    email: str,
):
    await state.update_data(email=message.text)
    # await state.set_state(Survey.email)
    await message.answer(
        text=f"Your email is {markdown.hbold(email)}",
    )


@router.message(Survey.full_name)
async def handle_user_full_name_invalid_type(message: Message, state: FSMContext):
    await message.answer(
        text="Send your name as a text",
    )


@router.message(Survey.email)
async def handle_user_invalid_email(message: Message, state: FSMContext):
    await message.answer(
        text="Invalid email",
    )
