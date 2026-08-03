from fastapi import APIRouter,Depends

from dependencies.dependencies import require_admin

router=APIRouter()

@router.get("/health")
def health():
    return {
        'status':'healthy'
    }