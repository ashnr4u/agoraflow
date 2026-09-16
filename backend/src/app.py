from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from models import Base

load_dotenv() # reads variables from a .env file and sets them in os.environ

user= os.getenv("DB_USER")
password= os.getenv("DB_password")

print("Debugging --------------------------------------")
db= create_engine(f"postgresql://{user}:{password}@localhost:5000/agoraflow")

# creates all ORM-defined tables in the database
Base.metadata.create_all(db)