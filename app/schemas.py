
from pydantic import BaseModel
from datetime import datetime


# --- Sensors ---
class SensorBase(BaseModel):
    name: str
    model: str | None = None

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
    location_id: int | None = None
    temperature: float | None = None
    humidity: float | None = None
    pressure: float | None = None
    co2: float | None = None

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
    location_id: int | None = None
    moisture: float | None = None

class SoilDataCreate(SoilDataBase):
    pass

class SoilData(SoilDataBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True
