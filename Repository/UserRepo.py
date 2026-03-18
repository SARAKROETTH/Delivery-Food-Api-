from Models.Auth.UserModel import User as UserModel
from sqlalchemy.orm import Session
from Schemas.UserSchemas import UserCreate as UserCreateSchema

def create_user(db: Session, user: UserCreateSchema):
    db_user = UserModel(
        username=user.username,
        phoneNumber=user.phoneNumber,
        imageUrl=user.imageUrl
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_all(db: Session):
    return db.query(UserModel).all()





