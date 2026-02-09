
import csv
import io
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    contents = await file.read()
    buffer = io.StringIO(contents.decode('utf-8'))
    csv_reader = csv.reader(buffer)
    header = next(csv_reader) # Skip header row

    if header != ['name', 'description']:
        raise HTTPException(status_code=400, detail="Invalid CSV header. Expected 'name,description'.")

    for row in csv_reader:
        item_data = schemas.ItemCreate(name=row[0], description=row[1])
        crud.create_item(db=db, item=item_data)

    buffer.close()

    return {"message": "CSV file imported successfully."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Homelab Webserver API!"}
