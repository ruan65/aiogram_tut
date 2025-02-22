import email
from aiogram.types import Message


def valid_email(value: str) -> str:
    if "@" not in value or "." not in value:
        raise ValueError("Invalid email")
    return value.lower()


def valid_email_filter(message: Message) -> str | None:
    try:
        email = valid_email(message.text)
    except ValueError:
        return None
    return {"email": email}
