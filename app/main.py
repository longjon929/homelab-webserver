import csv
import io
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from . import crud, schemas
from .database import get_db_connection

app = FastAPI()

# Dependency
def get_db_conn():
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()

# --- Sensors ---
@app.post("/sensors/", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, conn = Depends(get_db_conn)):
    return crud.create_sensor(conn=conn, sensor=sensor)

@app.get("/sensors/", response_model=list[schemas.Sensor])
def read_sensors(skip: int = 0, limit: int = 100, conn = Depends(get_db_conn)):
    return crud.get_sensors(conn, skip=skip, limit=limit)

@app.get("/sensors/{sensor_id}", response_model=schemas.Sensor)
def read_sensor(sensor_id: int, conn = Depends(get_db_conn)):
    db_sensor = crud.get_sensor(conn, sensor_id=sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

# --- Locations ---
@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, conn = Depends(get_db_conn)):
    return crud.create_location(conn=conn, location=location)

@app.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, conn = Depends(get_db_conn)):
    return crud.get_locations(conn, skip=skip, limit=limit)

@app.get("/locations/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, conn = Depends(get_db_conn)):
    db_location = crud.get_location(conn, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

# --- Environment Data ---
@app.post("/environment-data/", response_model=schemas.EnvironmentData)
def create_environment_data(data: schemas.EnvironmentDataCreate, conn = Depends(get_db_conn)):
    return crud.create_environment_data(conn=conn, data=data)

@app.get("/environment-data/", response_model=list[schemas.EnvironmentData])
def read_environment_data(skip: int = 0, limit: int = 100, conn = Depends(get_db_conn)):
    return crud.get_environment_data_list(conn, skip=skip, limit=limit)

@app.get("/environment-data/{data_id}", response_model=schemas.EnvironmentData)
def read_single_environment_data(data_id: int, conn = Depends(get_db_conn)):
    data = crud.get_environment_data(conn, env_id=data_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Environment data not found")
    return data

# --- Soil Data ---
@app.post("/soil-data/", response_model=schemas.SoilData)
def create_soil_data(data: schemas.SoilDataCreate, conn = Depends(get_db_conn)):
    return crud.create_soil_data(conn=conn, data=data)

@app.get("/soil-data/", response_model=list[schemas.SoilData])
def read_soil_data(skip: int = 0, limit: int = 100, conn = Depends(get_db_conn)):
    return crud.get_soil_data_list(conn, skip=skip, limit=limit)

@app.get("/soil-data/{data_id}", response_model=schemas.SoilData)
def read_single_soil_data(data_id: int, conn = Depends(get_db_conn)):
    data = crud.get_soil_data(conn, soil_id=data_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Soil data not found")
    return data

# @app.post("/upload-csv/")
# async def upload_csv(file: UploadFile = File(...), conn = Depends(get_db_conn)):
#     if not file.filename.endswith('.csv'):
#         raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

#     contents = await file.read()
#     buffer = io.StringIO(contents.decode('utf-8'))
#     csv_reader = csv.reader(buffer)
#     header = next(csv_reader) # Skip header row

#     if header != ['name', 'description']:
#         raise HTTPException(status_code=400, detail="Invalid CSV header. Expected 'name,description'.")

#     for row in csv_reader:
#         item_data = schemas.ItemCreate(name=row[0], description=row[1])
#         crud.create_item(conn=conn, item=item_data)

#     buffer.close()

#     return {"message": "CSV file imported successfully."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Homelab Webserver API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)