from typing import *

from pydantic import BaseModel, Field


class DailyResponse(BaseModel):
    """
    None model

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    time: List[str] = Field(validation_alias="time")

    temperature_2m_max: Optional[List[float]] = Field(validation_alias="temperature_2m_max", default=None)

    temperature_2m_min: Optional[List[float]] = Field(validation_alias="temperature_2m_min", default=None)

    apparent_temperature_max: Optional[List[float]] = Field(validation_alias="apparent_temperature_max", default=None)

    apparent_temperature_min: Optional[List[float]] = Field(validation_alias="apparent_temperature_min", default=None)

    precipitation_sum: Optional[List[float]] = Field(validation_alias="precipitation_sum", default=None)

    precipitation_hours: Optional[List[float]] = Field(validation_alias="precipitation_hours", default=None)

    weather_code: Optional[List[float]] = Field(validation_alias="weather_code", default=None)

    sunrise: Optional[List[str]] = Field(validation_alias="sunrise", default=None)

    sunset: Optional[List[str]] = Field(validation_alias="sunset", default=None)

    wind_speed_10m_max: Optional[List[float]] = Field(validation_alias="wind_speed_10m_max", default=None)

    wind_gusts_10m_max: Optional[List[float]] = Field(validation_alias="wind_gusts_10m_max", default=None)

    wind_direction_10m_dominant: Optional[List[float]] = Field(
        validation_alias="wind_direction_10m_dominant", default=None
    )

    shortwave_radiation_sum: Optional[List[float]] = Field(validation_alias="shortwave_radiation_sum", default=None)

    uv_index_max: Optional[List[float]] = Field(validation_alias="uv_index_max", default=None)

    uv_index_clear_sky_max: Optional[List[float]] = Field(validation_alias="uv_index_clear_sky_max", default=None)

    et0_fao_evapotranspiration: Optional[List[float]] = Field(
        validation_alias="et0_fao_evapotranspiration", default=None
    )
