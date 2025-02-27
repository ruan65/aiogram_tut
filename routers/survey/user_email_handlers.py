from aiogram import F, Router
from aiogram.utils import markdown
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from email_validator import EmailNotValidError, validate_email

from keyboards.common_keyboards import build_select_keyboard, build_yes_no_keyboard
from routers.survey.states import Sports, Survey


router = Router(name=__name__)


@router.message(
    Survey.email,
    # valid_email_filter,
    # F.func(valid_email_or_none).as_("email"),
    F.text.cast(validate_email).normalized.as_("email"),
)
async def handle_user_email(
    message: Message,
    state: FSMContext,
    email: str,
):
    print(f"valid email: {F.text.cast(validate_email).normalized}")
    await state.update_data(email=email)
    await state.set_state(Survey.sport)
    await message.answer(
        text=(f"Your email is {markdown.hcode(email)}\nWhat sport do you prefer?"),
        reply_markup=build_select_keyboard(Sports),
    )


@router.message(Survey.email_newsletter, F.text.casefold() == "yes")
async def handle_user_email_newsletter(message: Message, state: FSMContext):
    data = await state.update_data(email_newsletter=True)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter, F.text.casefold() == "no")
async def handle_user_email_newsletter_not_ok(message: Message, state: FSMContext):
    data = await state.update_data(email_newsletter=False)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter)
async def handle_user_email_newsletter_unknown(message: Message):
    await message.answer(
        text=(
            "Sorry, I don't understand, "
            f"send {markdown.hcode('yes')} or {markdown.hcode('no')}"
        ),
        reply_markup=build_yes_no_keyboard(),
    )


@router.message(Survey.full_name)
async def handle_user_full_name_invalid_type(message: Message, state: FSMContext):
    await message.answer(
        text="Send your name as a text",
    )


@router.message(Survey.email)
async def handle_user_invalid_email(message: Message, state: FSMContext):
    await message.answer(
        text="Invalid email. Cansel survey: /cancel",
    )


async def send_survey_results(message: Message, data: dict) -> None:
    text = markdown.text(
        "Your survey results:",
        markdown.text("Name:", markdown.hbold(data["full_name"])),
        markdown.text("Email:", markdown.hbold(data["email"])),
        markdown.text(
            (
                "Cool, we will send you newsletter"
                if data["email_newsletter"]
                else "We won't send you newsletter"
            ),
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove(),
    )
