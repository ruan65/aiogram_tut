import email
from aiogram.types import Message
from email_validator import EmailNotValidError, validate_email


def valid_email_filter(message: Message) -> str | None:
    try:
        email = validate_email(message.text)
    except EmailNotValidError:
        return None
    return {"email": email.normalized}
