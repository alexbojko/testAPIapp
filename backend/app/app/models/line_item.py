from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

from sqlalchemy import Table

line_item = Table(
    'lineitem', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('line_id', ForeignKey('line.id'), primary_key=True),
    Column('item_id', ForeignKey('item.id'), primary_key=True),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now),
    Column('owner_id', Integer, ForeignKey("user.id")),
)


class LineItem(Base):
    __table__ = line_item
