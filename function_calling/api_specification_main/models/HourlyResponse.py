from typing import *

from pydantic import BaseModel, Field


class HourlyResponse(BaseModel):
    """
    None model

    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    time: List[str] = Field(validation_alias="time")

    temperature_2m: Optional[List[float]] = Field(validation_alias="temperature_2m", default=None)

    relative_humidity_2m: Optional[List[float]] = Field(validation_alias="relative_humidity_2m", default=None)

    dew_point_2m: Optional[List[float]] = Field(validation_alias="dew_point_2m", default=None)

    apparent_temperature: Optional[List[float]] = Field(validation_alias="apparent_temperature", default=None)

    pressure_msl: Optional[List[float]] = Field(validation_alias="pressure_msl", default=None)

    cloud_cover: Optional[List[float]] = Field(validation_alias="cloud_cover", default=None)

    cloud_cover_low: Optional[List[float]] = Field(validation_alias="cloud_cover_low", default=None)

    cloud_cover_mid: Optional[List[float]] = Field(validation_alias="cloud_cover_mid", default=None)

    cloud_cover_high: Optional[List[float]] = Field(validation_alias="cloud_cover_high", default=None)

    wind_speed_10m: Optional[List[float]] = Field(validation_alias="wind_speed_10m", default=None)

    wind_speed_80m: Optional[List[float]] = Field(validation_alias="wind_speed_80m", default=None)

    wind_speed_120m: Optional[List[float]] = Field(validation_alias="wind_speed_120m", default=None)

    wind_speed_180m: Optional[List[float]] = Field(validation_alias="wind_speed_180m", default=None)

    wind_direction_10m: Optional[List[float]] = Field(validation_alias="wind_direction_10m", default=None)

    wind_direction_80m: Optional[List[float]] = Field(validation_alias="wind_direction_80m", default=None)

    wind_direction_120m: Optional[List[float]] = Field(validation_alias="wind_direction_120m", default=None)

    wind_direction_180m: Optional[List[float]] = Field(validation_alias="wind_direction_180m", default=None)

    wind_gusts_10m: Optional[List[float]] = Field(validation_alias="wind_gusts_10m", default=None)

    shortwave_radiation: Optional[List[float]] = Field(validation_alias="shortwave_radiation", default=None)

    direct_radiation: Optional[List[float]] = Field(validation_alias="direct_radiation", default=None)

    direct_normal_irradiance: Optional[List[float]] = Field(validation_alias="direct_normal_irradiance", default=None)

    diffuse_radiation: Optional[List[float]] = Field(validation_alias="diffuse_radiation", default=None)

    vapour_pressure_deficit: Optional[List[float]] = Field(validation_alias="vapour_pressure_deficit", default=None)

    evapotranspiration: Optional[List[float]] = Field(validation_alias="evapotranspiration", default=None)

    precipitation: Optional[List[float]] = Field(validation_alias="precipitation", default=None)

    weather_code: Optional[List[float]] = Field(validation_alias="weather_code", default=None)

    snow_height: Optional[List[float]] = Field(validation_alias="snow_height", default=None)

    freezing_level_height: Optional[List[float]] = Field(validation_alias="freezing_level_height", default=None)

    soil_temperature_0cm: Optional[List[float]] = Field(validation_alias="soil_temperature_0cm", default=None)

    soil_temperature_6cm: Optional[List[float]] = Field(validation_alias="soil_temperature_6cm", default=None)

    soil_temperature_18cm: Optional[List[float]] = Field(validation_alias="soil_temperature_18cm", default=None)

    soil_temperature_54cm: Optional[List[float]] = Field(validation_alias="soil_temperature_54cm", default=None)

    soil_moisture_0_1cm: Optional[List[float]] = Field(validation_alias="soil_moisture_0_1cm", default=None)

    soil_moisture_1_3cm: Optional[List[float]] = Field(validation_alias="soil_moisture_1_3cm", default=None)

    soil_moisture_3_9cm: Optional[List[float]] = Field(validation_alias="soil_moisture_3_9cm", default=None)

    soil_moisture_9_27cm: Optional[List[float]] = Field(validation_alias="soil_moisture_9_27cm", default=None)

    soil_moisture_27_81cm: Optional[List[float]] = Field(validation_alias="soil_moisture_27_81cm", default=None)
