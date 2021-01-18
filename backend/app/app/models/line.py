from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# from .line_item import line_item
from .mixins import AuditMixin

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Line(Base, AuditMixin):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="lines")
    # items =[]
    items = relationship(
        "Item",
        secondary="lineitem",
        back_populates="lines"
    )
    line_items = relationship("LineItem", backref="line", )
