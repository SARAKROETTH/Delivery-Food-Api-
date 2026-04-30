from fastapi import FastAPI,Depends
from fastapi.responses import JSONResponse

from Config.DatabaseConfig import engine, Base

from Config.DatabaseConfig import get_db

from fastapi.middleware.cors import CORSMiddleware




from Routes.UploadRoutes import router as image_router
from Routes.AdminAuthRoutes import router as admin_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(admin_router)

app.include_router(image_router)



# Create tables automatically
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "/docs to see API documentation and /auth/user to test database connection"}
