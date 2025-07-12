from fastapi import FastAPI
from app.routes import users, items, swaps,redeems

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(swaps.router)
app.include_router(redeems.router)

