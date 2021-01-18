from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Sequence, String, DateTime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from ..db.session import engine

if TYPE_CHECKING:
    from .user import User  # noqa: F401

from sqlalchemy import Table, Text

line_item = Table(
    'lineitem', Base.metadata,
    # Column('id', Integer, primary_key=True, index=True, autoincrement=True),
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('line_id', ForeignKey('line.id'), primary_key=True),
    Column('item_id', ForeignKey('item.id'), primary_key=True),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now),
    Column('owner_id', Integer, ForeignKey("user.id")),
)


class LineItem(Base):
    __table__ = line_item
