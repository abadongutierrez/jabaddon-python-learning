from typing import *

from pydantic import BaseModel, Field


class CurrentWeather(BaseModel):
    """
    None model

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    time: str = Field(validation_alias="time")

    temperature: float = Field(validation_alias="temperature")

    wind_speed: float = Field(validation_alias="wind_speed")

    wind_direction: float = Field(validation_alias="wind_direction")

    weather_code: float = Field(validation_alias="weather_code")
