from fastapi import FastAPI,Depends
from fastapi.responses import JSONResponse

from Config.DatabaseConfig import engine, Base

from Config.DatabaseConfig import get_db

from Models.Auth.UserModel import User as UserModel


from Routes.AuthRoutes import router as auth_router
app = FastAPI()


app.include_router(auth_router)

# Create tables automatically
UserModel.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "/docs to see API documentation and /auth/user to test database connection"}
