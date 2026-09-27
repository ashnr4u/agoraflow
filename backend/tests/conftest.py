import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app import app
from database import get_db
from models import Base

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

TEST_DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@localhost:5000/agoraflow_test"
)

test_engine = create_engine(TEST_DATABASE_URL)

TestSession = sessionmaker(bind=test_engine)

Base.metadata.create_all(test_engine)


def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def clean_test_db():
    db = TestSession()
    try:
        for table in reversed(Base.metadata.sorted_tables):
            db.execute(table.delete())
        db.commit()
    finally:
        db.close()


@pytest.fixture(autouse=True)
def reset_database():
    clean_test_db()