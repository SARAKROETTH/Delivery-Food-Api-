from Models.Auth.UserModel import User as UserModel
from sqlalchemy.orm import Session
from Schemas.UserSchemas import AdminCreate,AdminRespone



def get_admin(db: Session):
    return db.query(UserModel).filter(UserModel.role == "admin").all

def create_admin(db: Session, admin:AdminCreate):
    db_admin = UserModel(
        
    )
    return db_admin
