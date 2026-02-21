import logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes import products_router, categories_router, cart_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url='/api/docs',
    redoc_url='/api/redoc'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.warning(f"📂 CWD (рабочая папка): {Path.cwd()}")
logging.warning(f"⚙️  settings.static_dir: {settings.static_dir}")
logging.warning(f"🔍 Абсолютный путь: {Path(settings.static_dir).resolve()}")
logging.warning(f"✅ Существует?: {Path(settings.static_dir).exists()}")

app.mount('/static', StaticFiles(directory=settings.static_dir), name='static')



app.include_router(products_router)
app.include_router(categories_router)
app.include_router(cart_router)

@app.on_event('startup')
def on_startup():
    init_db()

@app.get('/')
def root():
    return {
        'message': 'Welcome to fastapi shop API',
        "docs": "api/docs",
    }

@app.get('/health')
def health_check():
    return {'status': 'healthy'}