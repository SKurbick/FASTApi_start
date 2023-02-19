from typing import List

from fastapi import APIRouter

from src.workshop import tables
from src.workshop.database import Session
from src.workshop.models.operations import Operation

router = APIRouter(
    prefix='/operations',
)


# , response_model=List[Operation]
@router.get('/', response_model=List[Operation])
def get_operations():
    session = Session()
    operations = (
        session
        .query(tables.Operation)
        .all()
    )
    return operations
