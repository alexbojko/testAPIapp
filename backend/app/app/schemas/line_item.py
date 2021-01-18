from typing import Optional

from pydantic import BaseModel


# Shared properties

class LineItemBase(BaseModel):
    line_id: int
    item_id: int

# Properties to receive on item creation
class LineItemCreate(BaseModel):
    item_id: int


# Properties to receive on item update
class LineItemUpdate(LineItemBase):
    pass


# Properties shared by models stored in DB
class LineItemInDBBase(LineItemBase):
    class Config:
        orm_mode = True


# Properties to return to client
class LineItem(LineItemInDBBase):
    id: int


# Properties properties stored in DB
class LineItemInDB(LineItemInDBBase):
    pass
    # line: Line
    # item: Item
