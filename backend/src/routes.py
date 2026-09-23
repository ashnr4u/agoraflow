
from models import User,Event,Registration
from database import get_db,password_hash
from schemas import UserCreate, CreateEvent, EventResponse,RegistrationCreate
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
                new_user.created_at = datetime.now()
        
                session.add(new_user)
                session.commit()

                return ("User Created Successfully")
        except IntegrityError:
                # If same-email repeats
                session.rollback()
                raise HTTPException(status_code=409, detail= "User's Email already exists")
        
        

@router.post("/create_event")
def create_event(event: CreateEvent, session = Depends(get_db)):
        try:
                new_event = Event()
                new_event.event_name = event.event_name
                new_event.max_capacity = event.max_capacity
                new_event.registration_start = event.registration_start
                new_event.registration_close = event.registration_close
                new_event.event_start_date = event.event_start_date
                new_event.description = event.description
                new_event.organizer_id = 41

                session.add(new_event)
                session.commit()      
                return {"message":"Even creation completed"}         

        except IntegrityError: 
                session.rollback() 
                raise HTTPException( status_code=409, detail="Event name already exists" )
                



@router.get("/event_list", response_model=list[EventResponse])
def get_events( session=Depends(get_db)):
        events_list = session.query(Event).all()
        return events_list

  
@router.post("/register")
def register_user( registration: RegistrationCreate, session=Depends(get_db)
):
    new_registration = Registration()

    new_registration.user_id = 41
    new_registration.event_id = registration.event_id
    new_registration.registered_at = datetime.now()

    session.add(new_registration)
    session.commit()

    return {"message": "Registration successful"}