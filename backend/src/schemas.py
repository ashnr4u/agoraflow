from pydantic import BaseModel,field_validator, Field,  ConfigDict
from datetime import datetime
# Pydantic field name and database field name don't have to be the same.
class UserCreate(BaseModel):
    user_email: str 
    users_name: str   
    password:str
    role: str

    @field_validator("user_email")
    @classmethod
    def validate_email(cls,user_email):
        user_email =user_email.lower()
        if user_email.endswith("@agoraflow"):
            return user_email
        else:
            raise ValueError("use your student email id ending with @agoraflow")

      
class CreateEvent(BaseModel):
    event_name: str
    max_capacity: int 
    registration_start: datetime
    registration_close : datetime
    event_start_date :datetime
    description: str = Field(max_length =200)



class EventResponse(BaseModel):
        event_name: str
        max_capacity: int 
        registration_start: datetime
        registration_close : datetime
        event_start_date :datetime
        description: str 

        # Allow Pydantic to read attributes from SQLAlchemy objects
        model_config = ConfigDict(from_attributes=True)

class RegistrationCreate(BaseModel):
    event_id: int

class UserLogin(BaseModel):
     username : str # we changed user_email to username to test authorization
     password :str