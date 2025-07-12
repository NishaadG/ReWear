import os
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session, joinedload
from app.database import SessionLocal
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()

UPLOAD_DIR = "../static/images"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Upload Image Endpoint
import os
from uuid import uuid4
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "static", "images")
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the path exists

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    ext = file.filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    # Public URL path (served from /static)
    image_url = f"http://localhost:8000/static/images/{filename}"
    return {"url": image_url}

# ✅ Create Item with image URLs
@router.post("/items/", response_model=schemas.ItemOut)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_item = models.Item(
        title=item.title,
        description=item.description,
        category=item.category,
        size=item.size,
        condition=item.condition,
        tags=item.tags,
        brand=item.brand,
        color=item.color,
        material=item.material,
        location=item.location,
        exchange_method=item.exchange_method,
        owner_id=current_user.id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    # Add linked image URLs
    for url in item.image_urls:
        db_image = models.ItemImage(item_id=db_item.id, url=url)
        db.add(db_image)

    db.commit()
    db.refresh(db_item)

    return db_item

# ✅ Get All Approved Items (with images)
@router.get("/items/", response_model=list[schemas.ItemOut])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).options(joinedload(models.Item.images))\
        .filter(models.Item.approved == True).all()
    return items

# ✅ Get Item by ID (with images)
@router.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).options(joinedload(models.Item.images))\
        .filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
