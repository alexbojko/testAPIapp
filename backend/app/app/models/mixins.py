from datetime import datetime
from sqlalchemy import Column, DateTime


class AuditMixin(object):
    """Mixin Class to add created_at and updated_at fields to the inherited class models."""

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)