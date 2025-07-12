from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    points: int
    role: str
    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    title: str
    description: str
    category: str
    size: str
    condition: str
    tags: str
    image_url: str
class Token(BaseModel):
    access_token: str
    token_type: str
class ItemOut(ItemCreate):
    id: int
    status: str
    owner_id: int
    class Config:
        orm_mode = True
class ItemCreate(BaseModel):
    title: str
    description: str
    category: str
    size: str
    condition: str
    tags: str
    image_url: str

class ItemOut(ItemCreate):
    id: int
    status: str
    owner_id: int

    class Config:
        from_attributes = True  # for Pydantic v2
class SwapRequestCreate(BaseModel):
    item_id: int

class SwapRequestOut(BaseModel):
    id: int
    item_id: int
    requester_id: int
    status: str

    class Config:
        from_attributes = True
