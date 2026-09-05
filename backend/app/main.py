from fastapi import FastAPI

from app.routers import connectivity_check_router


app = FastAPI()


app.include_router(connectivity_check_router)


