from fastapi import FastAPI,Depends
from fastapi.responses import JSONResponse

from Config.DatabaseConfig import get_db
from sqlalchemy.orm import Session
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user")
async def get_user(db: Session = Depends(get_db)):
    return JSONResponse(content={"message": "User endpoint", "db_status": "Connected", "db_url": str(db.bind.url)})