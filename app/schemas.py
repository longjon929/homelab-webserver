from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# --- Sensors ---
class SensorBase(BaseModel):
    name: str
    model: Optional[str] = None


class SensorCreate(SensorBase):
    pass


class Sensor(SensorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# --- Locations ---
class LocationBase(BaseModel):
    name: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# --- Environment Data ---
class EnvironmentDataBase(BaseModel):
    sensor_id: int
    location_id: int
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None
    co2: Optional[float] = None


class EnvironmentDataCreate(EnvironmentDataBase):
    pass


class EnvironmentData(EnvironmentDataBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True


# --- Soil Data ---
class SoilDataBase(BaseModel):
    sensor_id: int
    location_id: int
    moisture: float
    adc: int


class SoilDataCreate(SoilDataBase):
    pass


class SoilData(SoilDataBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True
