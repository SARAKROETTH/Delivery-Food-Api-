from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.DatabaseConfig import get_db
from Repository.UserRepo import get_admin
from Models.Auth.UserModel import User as UserModel

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/admin")
async def get_admins(db: Session = Depends(get_db)):
    admin = get_admin(db)
    return admin

