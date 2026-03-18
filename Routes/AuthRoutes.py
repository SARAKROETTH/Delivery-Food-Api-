from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.DatabaseConfig import get_db
from Repository.UserRepo import get_user_all, create_user, get_user_by_id, delete_user_by_id
from Schemas.UserSchemas import UserCreate as UserCreateSchema
from Models.Auth.UserModel import User as UserModel

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/user")
async def get_user(db: Session = Depends(get_db)):
    users = get_user_all(db)
    return {"message": "User endpoint", "db_status": "Connected", "users": users}

@router.post("/user")
async def create_user(db: Session = Depends(get_db),user : UserCreateSchema = Depends()):
    new_user = create_user(db, user)
    return {"message": "User created successfully", "user": new_user}
    
#  get user by id
@router.get("/user/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user:
        return {"message": "User found", "user": user}
    else:
        return {"message": "User not found"}
    

# delete user by id
@router.delete("/user/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    success = delete_user_by_id(db, user_id)
    
    if success:
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
