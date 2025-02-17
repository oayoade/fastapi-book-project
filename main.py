from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router

from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
