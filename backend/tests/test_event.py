# TODO: Implement API tests for /create_event:
# 1. Organizer successfully creates an event -> 200
# 2. Organizer creates duplicate event name -> 409
# 3. Student attempts to create an event -> 403
# 4. Unauthenticated user attempts to create an event -> 401
# 5. Invalid event payload -> 422
print("test_event.py")

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)
'''
@router.post("/create_event")
def create_event(event: CreateEvent, 
                 current_user =Depends(require_organizer),session = Depends(get_db)):

class CreateEvent(BaseModel):
    event_name: str
    max_capacity: int 
    registration_start: datetime
    registration_close : datetime
    event_start_date :datetime
    description: str = Field(max_length =200)


'''
def test_create_event():
    response = client.post("/create_event",
                        json={
                                "event_name" : "event1" ,
                                "max_capacity" :   "100",
                                "registration_start" : 11-11-2026,
                                "registration_close " :  11-11-2028,
                                "event_start_date " : 11-12-2026,
                                "description"  : "whatever man"

                        }
                
                    )