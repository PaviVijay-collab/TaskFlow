from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleCreate, RoleResponse
from app.services.authorization import require_role


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post(
    "",
    response_model=RoleResponse,
    status_code=status.HTTP_201_CREATED
)
def create_role(
    role_data: RoleCreate,
    current_user: User = Depends(
        require_role("Admin")
    ),
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Role).where(
            Role.name == role_data.name
        )
    )

    existing_role = result.scalar_one_or_none()

    if existing_role:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Role already exists"
        )

    role = Role(
        name=role_data.name
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role