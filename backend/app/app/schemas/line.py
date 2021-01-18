from typing import Optional

from pydantic import BaseModel


# Shared properties
class LineBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class LineCreate(LineBase):
    title: str


# Properties to receive on item update
class LineUpdate(LineBase):
    pass


# Properties shared by models stored in DB
class LineInDBBase(LineBase):
    id: int
    title: str
    owner_id: int
    # items: Any

    class Config:
        orm_mode = True


# Properties to return to client
class Line(LineInDBBase):
    items: Optional[list]
    # pass


# Properties properties stored in DB
class LineInDB(LineInDBBase):
    items: list
    pass
