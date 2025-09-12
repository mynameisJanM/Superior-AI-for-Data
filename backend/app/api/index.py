from fastapi import FastAPI
from app.api import router  # Adjust import
from app.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router, prefix="/api")

# Vercel expects a WSGI app; use asgi for FastAPI
def handler(request):
    from mangum import Mangum  # Add 'mangum==0.17.0' to requirements.txt
    asgi_app = app
    return Mangum(asgi_app)(request)