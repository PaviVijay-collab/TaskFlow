# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app.database import get_db
# from app.models.user import User
# from app.models.role import Role
# from app.schemas.user import UserCreate, UserResponse
# from app.services.security import hash_password
# from fastapi.security import OAuth2PasswordRequestForm
# from app.services.security import hash_password, verify_password
# from app.services.jwt import create_access_token

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.role import Role
from app.schemas.user import UserCreate, UserResponse
from app.services.security import hash_password, verify_password
from app.services.jwt import create_access_token
from app.services.auth import get_current_user
from app.services.authorization import require_role

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    # Check whether email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Check whether role exists
    role = (
        db.query(Role)
        .filter(Role.id == user_data.role_id)
        .first()
    )

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid role_id"
        )

    # Hash password
    hashed_password = hash_password(user_data.password)

    # Create user
    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
        role_id=user_data.role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@router.get("/developer-only")
def developer_only(
    current_user: User = Depends(
        require_role("Developer")
    )
):
    return {
        "message": "You are a Developer",
        "user": current_user.name
    }

@router.get("/admin-only")
def admin_only(
    current_user: User = Depends(
        require_role("Admin")
    )
):
    return {
        "message": "You are an Admin",
        "user": current_user.name
    }