
from models import User,Event,Registration
from database import get_db,password_hash
from schemas import UserCreate, CreateEvent, EventResponse,RegistrationCreate,UserLogin
from fastapi import Depends,APIRouter, HTTPException,Request
from datetime import datetime, timezone, timedelta
from sqlalchemy.exc import IntegrityError
import os, jwt
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

load_dotenv()
jwt_secret_key = os.getenv("JWT_SECRET")

#extraxts jwt from bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

router = APIRouter()

#get token from oauth and decode it to get the user
def get_token(token=Depends(oauth2_scheme),session=Depends(get_db)):
    token = jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
    #jwt.decode() returns a Python dictionary

    user_id_token= token['sub']
    user_logged = session.query(User).filter(User.user_id==user_id_token).first()
    print("the role of user logged",user_logged.role)
    return user_logged

#check thea authorization 
def require_organizer(current_user=Depends(get_token)):
    if current_user.role != "organiser":
        raise HTTPException(
            status_code=403,
            detail="Only organisers can perform this action"
        )

    return current_user #retun user object

#dependency whose responsibility is to check user role as student
def require_student(current_user=Depends(get_token)):
    if current_user.role != "student":
                raise HTTPException(
                    status_code =403,
                    detail = "Only students can perform this action"
                )
    return current_user #retun user object after checking the role


@router.get("/test_get_token")
def test_get_token(token=Depends(get_token)):
    return {"message": "works"}



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
        
        
# auth required - access to organiser
@router.post("/create_event")
def create_event(event: CreateEvent, 
                 current_user =Depends(require_organizer),session = Depends(get_db)):
        try:
                
                new_event = Event()
                new_event.event_name = event.event_name
                new_event.max_capacity = event.max_capacity
                new_event.registration_start = event.registration_start
                new_event.registration_close = event.registration_close
                new_event.event_start_date = event.event_start_date
                new_event.description = event.description
                # new_event.organizer_id = 41
                new_event.organizer_id = current_user.user_id
          


                session.add(new_event)
                session.commit()      
                return {"message":"Even creation completed"}         

        except IntegrityError: 
                session.rollback() 
                raise HTTPException( status_code=409, detail="Event name already exists" )
                


#get event lust(Anyone can have it)
@router.get("/event_list", response_model=list[EventResponse])
def get_events( session=Depends(get_db)):
        events_list = session.query(Event).all()
        return events_list

# auth required
@router.post("/register")
def register_user( registration: RegistrationCreate, user_from_token =Depends(require_student),
                  session=Depends(get_db)
):
    new_registration = Registration()

    # new_registration.user_id = 41
    new_registration.user_id = user_from_token.user_id

    new_registration.event_id = registration.event_id
    new_registration.registered_at = datetime.now()

    session.add(new_registration)
    session.commit()

    return {"message": "Registration successful"}


#login_endpoint
@router.post("/login")
def login(credentials: OAuth2PasswordRequestForm = Depends(), session=Depends(get_db)):
    email = credentials.username
    password = credentials.password

    user = session.query(User).filter(User.user_email == email).first()

    if password_hash.verify(password, user.hashed_password):

        # If password is verified, create a token to send to the client
        payload = {
            "sub": str(user.user_id),
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }

        token = jwt.encode(
            payload,
            jwt_secret_key,
            algorithm="HS256"
        )

    return {"access_token": token}




