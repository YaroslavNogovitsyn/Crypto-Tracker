import uvicorn
from fastapi import FastAPI

from backend.src.router import router as crypto_router

app = FastAPI()

app.include_router(crypto_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True, workers=3)
