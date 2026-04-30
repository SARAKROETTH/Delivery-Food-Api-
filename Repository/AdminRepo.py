from Midleware.security import hash_password
from Models.Auth.AdminModel import Admin as AdminModel
from sqlalchemy.orm import Session
from Schemas.AdminSchemas import AdminCreate


def get_admin(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AdminModel).offset(skip).limit(limit).all()

def create_admin(db: Session, admin: AdminCreate):
    new_admin = AdminModel(
        username=admin.username,
        email=admin.email,
        password=hash_password(admin.password),
        image_url=admin.image_url
    )

    db.add(new_admin)
    db.commit()                # ✅ execute
    db.refresh(new_admin)      # ✅ reload from DB

    return new_admin  


def get_admin_by_email(db:Session ,email:str):
    return db.query(AdminModel).filter(AdminModel.email == email).first()
