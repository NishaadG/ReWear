from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Swap Request
@router.post("/swap/request", response_model=schemas.SwapRequestOut)
def create_swap(req: schemas.SwapRequestCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    item = db.query(models.Item).filter(models.Item.id == req.item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot request your own item")

    # Prevent duplicate swap requests
    existing = db.query(models.SwapRequest).filter_by(item_id=req.item_id, requester_id=current_user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already requested")

    swap = models.SwapRequest(item_id=req.item_id, requester_id=current_user.id)
    db.add(swap)
    db.commit()
    db.refresh(swap)
    return swap

# View My Swap Requests
@router.get("/swap/mine", response_model=list[schemas.SwapRequestOut])
def my_swaps(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.SwapRequest).filter(models.SwapRequest.requester_id == current_user.id).all()

# Accept a Swap Request (owner only)
@router.put("/swap/{swap_id}/accept", response_model=schemas.SwapRequestOut)
def accept_swap(swap_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    swap = db.query(models.SwapRequest).filter(models.SwapRequest.id == swap_id).first()
    if not swap:
        raise HTTPException(status_code=404, detail="Swap not found")
    if swap.item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your item")

    swap.status = "accepted"
    swap.item.status = "swapped"
    db.commit()
    return swap

# Cancel Swap Request
@router.delete("/swap/{swap_id}/cancel")
def cancel_swap(swap_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    swap = db.query(models.SwapRequest).filter(models.SwapRequest.id == swap_id).first()
    if not swap or swap.requester_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to cancel")
    swap.status = "cancelled"
    db.commit()
    return {"message": "Cancelled"}
