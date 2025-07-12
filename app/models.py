from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Enum,DateTime,func
from sqlalchemy.orm import relationship
from .database import Base

class ItemImage(Base):
    __tablename__ = "item_images"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"))
    url = Column(String, nullable=False)

    item = relationship("Item", back_populates="images")


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
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=True)         # e.g., Tops, Bottoms, Accessories
    size = Column(String, nullable=True)             # e.g., M, L, XL
    condition = Column(String, nullable=True)        # e.g., New, Like New, Used
    tags = Column(String, nullable=True)             # comma-separated tags
    image_url = Column(String, nullable=False)       # hosted image path or S3 link
    status = Column(String, default="available")     # available / swapped / redeemed
    approved = Column(Boolean, default=False)        # For admin approval
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # 🔽 Newly added
    brand = Column(String, nullable=True)            # e.g., H&M, Nike
    color = Column(String, nullable=True)            # Dominant color (e.g., Red)
    material = Column(String, nullable=True)         # e.g., Cotton, Wool
    location = Column(String, nullable=True)         # e.g., Pune, Mumbai
    exchange_method = Column(String, default="both") # swap / redeem / both
    views = Column(Integer, default=0)               # Track how many times an item was viewed
    
    images = relationship("ItemImage", back_populates="item", cascade="all, delete")

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
