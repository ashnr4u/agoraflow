from pydantic import BaseModel,field_validator
from pydantic import BaseModel

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
        
        
  