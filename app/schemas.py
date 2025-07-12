from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# -----------------------------
# USER SCHEMAS
# -----------------------------

class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    phone: str
    address: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    name: str
    phone: str
    address: str
    points: int
    role: str

    class Config:
        from_attributes = True


# -----------------------------
# ITEM SCHEMAS
# -----------------------------

class ItemCreate(BaseModel):
    title: str
    description: str
    category: str
    size: str
    condition: str
    tags: str
    image_url: str
    brand: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    location: Optional[str] = None
    exchange_method: Optional[str] = Field(default="both")  # swap / redeem / both

class ItemOut(ItemCreate):
    id: int
    status: str
    approved: bool
    views: int
    owner_id: int

    class Config:
        from_attributes = True


# -----------------------------
# AUTH TOKEN
# -----------------------------

class Token(BaseModel):
    access_token: str
    token_type: str


# -----------------------------
# SWAP & REDEEM SCHEMAS
# -----------------------------

class SwapRequestCreate(BaseModel):
    item_id: int

class SwapRequestOut(BaseModel):
    id: int
    item_id: int
    requester_id: int
    status: str

    class Config:
        from_attributes = True

class RedeemRequest(BaseModel):
    item_id: int
    points_used: int

class RedemptionOut(BaseModel):
    id: int
    item_id: int
    user_id: int
    points_used: int
    status: str

    class Config:
        from_attributes = True



class ItemImageCreate(BaseModel):
    url: str

class ItemImageOut(BaseModel):
    id: int
    url: str

    class Config:
        from_attributes = True