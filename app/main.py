from fastapi import FastAPI
from app.routes import users, items, swaps

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(swaps.router)
