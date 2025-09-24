from fastapi import APIRouter
from .auth import router as AuthRouter

SystemRouter = APIRouter()

SystemRouter.include_router(AuthRouter, prefix="/auth", tags=["系统认证"])
