from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    points = Column(Integer, default=0)
    name = Column(String)
    phone = Column(String)
    address = Column(String)

    role = Column(String, default="user")  # or "admin"
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    size = Column(String)
    condition = Column(String)
    tags = Column(String)
    image_url = Column(String)
    status = Column(String, default="available")  # available / swapped / redeemed
    approved = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")

class SwapRequest(Base):
    __tablename__ = "swap_requests"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    requester_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")  # pending, accepted, rejected, cancelled

    item = relationship("Item")
    requester = relationship("User")

class Redemption(Base):
    __tablename__ = "redemptions"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    points_used = Column(Integer)
    status = Column(String, default="completed")  # could also track 'pending'

    item = relationship("Item")
    user = relationship("User")
