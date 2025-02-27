from enum import StrEnum
from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    full_name = State()
    email = State()
    sport = State()
    email_newsletter = State()


class SurveySportDetails(StatesGroup):
    tennis = State()
    football = State()
    basketball = State()
    formulaOne = State()


class Sports(StrEnum):
    tennis = "Tennis"
    football = "Football"
    basketball = "Basketball"
    formulaOne = "Formula One"


class KnownF1Tracks(StrEnum):
    bahrain = "Bahrain"
    algarve = "Algarve"
    imola = "Imola"
    monaco = "Monaco"
    spain = "Spain"
    suzuka = "Suzuka"
    spa = "Spa"
    monza = "Monza"
    hungaroring = "Hungaroring"
    abu_dhabi = "Abu Dhabi"
