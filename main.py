from fastapi import FastAPI
import uvicorn

from src.db.connection import database
from src.endpoints.retrieve import router

app = FastAPI()


@app.on_event("startup")
async def startup():
    print('[INFO] Connecting database')
    await database.connect()
    print('[INFO]  connected success!')

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def home():
    return {'status': 'OK'}

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)