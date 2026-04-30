from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from Config.DatabaseConfig import get_db
from Repository.AdminRepo import get_admin,create_admin,get_admin_by_email
from Schemas.AdminSchemas import AdminCreate,TokenResponse,LoginRequest

from Midleware.security import verify_password,create_access_token

router = APIRouter(prefix="/admin", tags=["admin"])



@router.get("/")
def get_admins(db:Session = Depends(get_db)):
    admin = get_admin(db)

    return {
        "status":"connected",
        "data": admin
        }

@router.post("/register")
def create_admin_route(
    admin: AdminCreate,
    db: Session = Depends(get_db)
):
    return create_admin(db, admin)

@router.post("/login",response_model=TokenResponse)
def login(data:LoginRequest,db: Session = Depends(get_db)):

    # call Repo to get user by email
    user = get_admin_by_email(db,data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        )
    
    if not verify_password(data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )
    
    token = create_access_token({"id":str(user.id)})


    return {
        "access_token": token,
        "token_type": "bearer"
    }



    
    
