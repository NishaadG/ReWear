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

# POST /redeem
@router.post("/redeem", response_model=schemas.RedemptionOut)
def redeem_item(req: schemas.RedeemRequest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    item = db.query(models.Item).filter(models.Item.id == req.item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.status != "available":
        raise HTTPException(status_code=400, detail="Item already taken")
    if item.owner_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot redeem your own item")

    if current_user.points < req.points_used:
        raise HTTPException(status_code=400, detail="Not enough points")

    # Re-fetch user within current DB session
    db_user = db.query(models.User).filter(models.User.id == current_user.id).first()
    db_user.points -= req.points_used

    redemption = models.Redemption(
        item_id=req.item_id,
        user_id=current_user.id,
        points_used=req.points_used
    )

    item.status = "redeemed"

    db.add(redemption)
    db.commit()
    db.refresh(redemption)
    return redemption


# GET /redeem/mine
@router.get("/redeem/mine", response_model=list[schemas.RedemptionOut])
def my_redemptions(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Redemption).filter(models.Redemption.user_id == current_user.id).all()
