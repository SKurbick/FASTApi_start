from fastapi import APIRouter
from src.workshop.api.operations import router as operations_router

router = APIRouter()
router.include_router(operations_router)
