
from models import User,Event,Registration
from database import get_db,password_hash
from schemas import UserCreate
from fastapi import Depends,APIRouter
from datetime import datetime, timezone
from sqlalchemy.exc import IntegrityError
router = APIRouter()
from fastapi import HTTPException

@router.post("/create_user" )
def create_user(user: UserCreate,session= Depends(get_db)):
        try:
                new_user = User()
                new_user.user_email = user.user_email
                new_user.name = user.users_name
                new_user.hashed_password = password_hash.hash(user.password)
                new_user.role = user.role
                new_user.created_at = datetime.now(timezone.utc)
        
                session.add(new_user)
                session.commit()

                return ("User Created Successfully")
        except IntegrityError:
                # If same-email repeats
                session.rollback()
                raise HTTPException(status_code=409, detail= "User's Email already exists")
        
        










