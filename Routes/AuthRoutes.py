from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.DatabaseConfig import get_db
from Models.Auth.UserModel import User as UserModel
from Schemas.UserSchemas import AdminCreate

router = APIRouter(prefix="/users", tags=["users"])


