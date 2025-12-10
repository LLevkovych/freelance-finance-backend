from fastapi import FastAPI
from app.database.session import engine

app = FastAPI()

@app.get("/ping")
async def ping():
    async with engine.begin() as conn:
        await conn.run_sync(lambda c: None)
    return {"status": "ok"}
