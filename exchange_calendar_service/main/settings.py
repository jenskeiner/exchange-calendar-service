from pydantic_settings import BaseSettings, SettingsConfigDict
import exchange_calendars as ec


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="EXCHANGE_CALENDAR_SERVICE_",
        env_nested_delimiter="__",
        env_file=".env",
    )

    changes_api_key: str | None = None

    # The optional full name of callable.
    init: str | None = None

    # The available exchanges.
    exchanges: dict[str, str] = {x: x for x in ec.calendar_utils.get_calendar_names(include_aliases=False)}


settings = Settings()
