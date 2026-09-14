from fastapi import FastAPI

from app.routers import connectivity_check_router
from app.routers.auth import router as auth_router

app = FastAPI()


app.include_router(connectivity_check_router)
app.include_router(auth_router)


