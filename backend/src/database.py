# To resolve circular dependency,(app-routes-app) databse will be defined seperately
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
load_dotenv()

db_user= os.getenv("DB_USER")
db_password= os.getenv("DB_PASSWORD")

db_engine = create_engine(f"postgresql://{db_user}:{db_password}@localhost:5000/agoraflow")
# creates all ORM-defined tables in the database
# Base.metadata.create_all(db_engine)

my_session = sessionmaker(bind = db_engine)
password_hash = PasswordHash.recommended()

def get_db():
    #my_session() creates a Session object through which I can perform database operations.
    db=my_session()
    try: 
        yield db

    finally:
        db.close()