from fastapi import APIRouter

from app.api.api_v1.endpoints import items, line_items, lines, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(lines.router, prefix="/lines", tags=["lines"])
api_router.include_router(line_items.router, prefix="/lines/{line_id}/items", tags=["line_items"])
