import email
from enum import StrEnum
from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    full_name = State()
    email = State()
    sport = State()
    email_newsletter = State()


class Sports(StrEnum):
    tennis = "Tennis"
    football = "Football"
    basketball = "Basketball"
    volleyball = "Volleyball"
