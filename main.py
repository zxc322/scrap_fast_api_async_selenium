from fastapi import FastAPI
import uvicorn

from db.connection import database

from api_routers import routers
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def home():
    return {'status': '44'}



app.include_router(routers.api_router)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)