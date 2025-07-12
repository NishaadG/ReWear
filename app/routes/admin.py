from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Item, User
from app.database import get_db
from app.dependencies import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

# Get all unapproved (pending) items
@router.get("/items/pending")
def get_pending_items(
    admin_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    return db.query(Item).filter(Item.approved == False).all()

# Approve a specific item
@router.patch("/items/{item_id}/approve")
def approve_item(
    item_id: int,
    admin_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.approved = True
    db.commit()
    return {"message": f"Item {item_id} approved"}

# Delete a specific item
@router.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    admin_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted"}
