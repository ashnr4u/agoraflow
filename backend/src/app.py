from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base
from fastapi import FastAPI, Depends

load_dotenv() # reads variables from a .env file and sets them in os.environ

user= os.getenv("DB_USER")
password= os.getenv("DB_PASSWORD")

print("Debugging --------------------------------------")
db_engine = create_engine(f"postgresql://{user}:{password}@localhost:5000/agoraflow")

# creates all ORM-defined tables in the database
# Base.metadata.create_all(db_engine)
app= FastAPI()

my_session = sessionmaker(bind = db_engine)
def get_db():
    #my_session() creates a Session object through which I can perform database operations.
    db=my_session()
    try: 
        yield db

    finally:
        db.close()

@app.get("/")
def test(test_db = Depends(get_db)):
    result = test_db.execute(text("Select 1"))
    value= result.scalar()
    return {"result":value}