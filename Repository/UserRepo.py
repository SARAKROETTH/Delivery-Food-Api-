from Models.Auth.UserModel import User as UserModel
from sqlalchemy.orm import Session
from Schemas.UserSchemas import UserCreate as UserCreateSchema


# create user
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

# get all users
def get_user_all(db: Session):
    return db.query(UserModel).all()

# get user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

# delete user by id
def delete_user_by_id(db: Session, user_id: int):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False