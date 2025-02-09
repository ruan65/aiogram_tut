import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # model_config = SettingsConfigDict(
    # case_sensitive=False
    # )

    TK_007: str
    admin_ids: frozenset[int] = frozenset({42, 134825803})


settings = Settings()


def fromEnv(var_name):
    return os.getenv(var_name)


TK = fromEnv("TK_007")
