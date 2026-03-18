from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.DatabaseConfig import get_db
from Repository.UserRepo import get_user_all

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/user")
async def get_user(db: Session = Depends(get_db)):
    users = get_user_all(db)
    return {"message": "User endpoint", "db_status": "Connected", "db_url": str(db.bind.url), "users": users}