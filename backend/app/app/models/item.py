from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .mixins import AuditMixin

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base, AuditMixin):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    
    line_items = relationship("LineItem", backref="item")
    
    lines = relationship(
        "Line",
        secondary="lineitem",
        back_populates="items"
    )
