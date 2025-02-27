from aiogram import F, Router
from aiogram.filters import Command
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
        SurveySportDetails.formulaOne,
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
    next_state, next_text = known_sport_to_next[message.text]
    await state.set_state(next_state)

    kb = ReplyKeyboardRemove()
    if message.text in known_sports_to_kb:
        kb = known_sports_to_kb[message.text]
    await message.answer(text=next_text, reply_markup=kb)


@router.message(
    Survey.sport,
)
async def unknown_sport(message: Message):
    await message.answer(
        text="Unknown sport, please select one of following:",
        reply_markup=build_select_keyboard(Sports),
    )
