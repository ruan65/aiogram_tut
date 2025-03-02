from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import ReplyKeyboardRemove

from keyboards.common_keyboards import build_select_keyboard
from routers.survey.states import KnownF1Tracks, Survey, Sports, SurveySportDetails

router = Router(name=__name__)

known_sport_to_next: dict[Sports | str, tuple[State, str]] = {
    Sports.tennis: (SurveySportDetails.tennis, "Who is your favorite tennis player?"),
    Sports.football: (
        SurveySportDetails.football,
        "What is your favorite football team?",
    ),
    Sports.basketball: (
        SurveySportDetails.basketball,
        "Who is your favorite basketball player?",
    ),
    Sports.formulaOne: (
        SurveySportDetails.formula_one,
        "What is your favorite fromula track?",
    ),
}

known_sports_to_kb: dict[Sports, str] = {
    Sports.formulaOne: build_select_keyboard(KnownF1Tracks),
}


@router.message(
    Survey.sport,
    F.text.cast(Sports),
)
async def select_sport(message: Message, state: FSMContext):
    await state.update_data(sport=message.text)
    next_state, question_text = known_sport_to_next[message.text]
    await state.update_data(sport=message.text, sport_question=question_text)
    await state.set_state(next_state)

    kb = ReplyKeyboardRemove()
    if message.text in known_sports_to_kb:
        kb = known_sports_to_kb[message.text]
    await message.answer(text=question_text, reply_markup=kb)


play_sports_filter = StateFilter(
    SurveySportDetails.basketball,
    SurveySportDetails.football,
    SurveySportDetails.tennis,
)


@router.message(
    F.text,
    play_sports_filter,
)
@router.message(
    F.text.cast(KnownF1Tracks),
    SurveySportDetails.formula_one,
)
async def handle_selected_sport_details_option(
    message: Message,
    state: FSMContext,
):
    await state.update_data(sport_details=message.text)
    await state.set_state(Survey.email_newsletter)
    await message.answer(
        text=(
            "Would you like to be nogified about this sport? Email newsletter?\n"
            "This is last step, but you can cancel survey: /cancel any time"
        ),
        reply_markup=build_select_keyboard(["Yes", "No"]),
    )


@router.message(play_sports_filter)
async def handle_sport_details_not_text(
    message: Message,
):
    await message.answer(
        text="Wee are sorry, but only text is allowed here",
    )


@router.message(SurveySportDetails.formula_one)
async def unknown_f1_track(message: Message):
    await message.answer(
        text="Unknown track, please select one of following:",
        reply_markup=build_select_keyboard(KnownF1Tracks),
    )


@router.message(
    Survey.sport,
)
async def unknown_sport(message: Message):
    await message.answer(
        text="Unknown sport, please select one of following:",
        reply_markup=build_select_keyboard(Sports),
    )
