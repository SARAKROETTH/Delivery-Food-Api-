from fastapi import FastAPI,Depends
from fastapi.responses import JSONResponse

from Config.DatabaseConfig import engine, Base

from Config.DatabaseConfig import get_db




from Routes.AuthRoutes import router as auth_router
from Routes.UploadRoutes import router as image_router


app = FastAPI()


app.include_router(auth_router)

app.include_router(image_router)

# Create tables automatically
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "/docs to see API documentation and /auth/user to test database connection"}
