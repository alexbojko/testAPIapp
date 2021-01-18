from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.line import Line
from app.schemas.line import LineCreate, LineUpdate


class CRUDItem(CRUDBase[Line, LineCreate, LineUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: LineCreate, owner_id: int
    ) -> Line:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Line]:
        return (
            db.query(self.model)
                .filter(Line.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )


line = CRUDItem(Line)
