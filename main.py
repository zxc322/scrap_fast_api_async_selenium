from fastapi import FastAPI
import uvicorn

from src.db.connection import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def home():
    return {'status': 'OK'}





if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)