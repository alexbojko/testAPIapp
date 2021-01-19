from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.models import Item, Line, LineItem
from uuid import uuid4
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    print("INITIAL USER", user)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    other_user = crud.user.get_by_email(
        db,
        email="other_test_user@mail.com"
    )
    print("OTHER USER", other_user)
    if not other_user:
        user_in = schemas.UserCreate(
            email="other_test_user@mail.com",
            password='123',
            is_superuser=False,
        )
        other_user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    lines = []

    print("USERS", user.__dict__, other_user.__dict__)
    print("GENERATING DATA")
    for current_user in [user, other_user]:
        print("\t FOR USER ", current_user.__dict__)
        for line_num in range(10):
            line: Line = Line(
                title=f"Line_{uuid4()}",
                description=f"Line description {uuid4()}",
                owner_id=current_user.id
            )
            print("\t\t GENERATED LINE", line.__dict__)
            for item_num in range(100):
                item = Item(
                    title=f"Item_{uuid4()}",
                    description=f"Item description {uuid4()}",
                    owner_id=current_user.id
                )
                line_item: LineItem = LineItem(
                    owner_id=current_user.id,
                    line=line,
                    item=item
                )
                line.line_items.append(line_item)
                print("\t\t\t GENERATED LINE ITEM", item.__dict__)
            lines.append(line)

    db.add_all(lines)
    db.commit()
