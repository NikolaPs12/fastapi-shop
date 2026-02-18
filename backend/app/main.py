from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes import products_router, categories_router, cart_router

app = FastAPI(title="FastAPI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories_router)
app.include_router(products_router)
app.include_router(cart_router)

@app.on_event("startup")
def startup_event():
    init_db()
