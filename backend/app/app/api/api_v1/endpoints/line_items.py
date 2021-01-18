from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas import LineItemInDB

router = APIRouter()


@router.post("/", response_model=schemas.LineItem)
def create_line_item(
        line_id: int,
        *,
        db: Session = Depends(deps.get_db),
        line_item_in: schemas.LineItemCreate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    line = crud.line.get(db=db, id=line_id)
    if not line:
        raise HTTPException(status_code=404, detail="Line not found")
    if not crud.user.is_superuser(current_user) and (line.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    item = crud.item.get(db=db, id=line_item_in.item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    # line.items.append(item)
    obj_to_db = LineItemInDB(line_id=line_id, **line_item_in.dict())
    line_item = crud.line_item.create_with_owner(db=db, obj_in=obj_to_db, owner_id=current_user.id)
    return line_item


@router.get("/", response_model=List[schemas.LineItem])
def read_line_items(
        line_id: int, *,
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    # if crud.user.is_superuser(current_user):
    line = crud.line.get(db=db, id=line_id)
    if not line:
        raise HTTPException(status_code=404, detail="Line not found")
    if not crud.user.is_superuser(current_user) and (line.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return crud.line_item.get_multi_for_line_by_owner(db, line_id=line_id, limit=limit, skip=skip, owner_id=current_user.id)


@router.delete("/{id}", response_model=schemas.Line)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.line_item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.line_item.remove(db=db, id=id)
    return item
