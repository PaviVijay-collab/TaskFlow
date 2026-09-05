from fastapi import APIRouter


router = APIRouter()


@router.get("/health-check")
def connectivity_check():
    return 'Fastapi server working successfully'