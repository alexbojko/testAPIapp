from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.line_item import LineItem
from app.schemas.line_item import LineItemCreate, LineItemUpdate


class CRUDItem(CRUDBase[LineItem, LineItemCreate, LineItemUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: LineItemCreate, owner_id: int
    ) -> LineItem:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[LineItem]:
        return (
            db.query(self.model)
            .filter(LineItem.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_for_line_by_owner(
            self, db: Session, line_id: int, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[LineItem]:
        return (
            db.query(self.model)
                .filter(LineItem.owner_id == owner_id, LineItem.line_id == line_id)
                .offset(skip)
                .limit(limit)
                .all()
        )


line_item = CRUDItem(LineItem)
