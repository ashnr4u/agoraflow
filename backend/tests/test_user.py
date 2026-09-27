from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)
#response_syntax = client.post("/endpoint", json={...})


def test_create_user():
    response = client.post(
        "/create_user",
        json={
            "users_name" : "pytest_user1",
            "user_email":  "pytest_user@agoraflow",
            "password": "TestPassword123",
            "role": "student"
        }
    )
    print("=========First Test Case=============")
    assert response.status_code == 200

def test_duplicate_email():

    response = client.post(
        "/create_user",
        json={
            "users_name" : "pytest_user2",
            "user_email":  "pytest_user2@agoraflow",
            "password": "TestPassword123",
            "role": "student"
        }
                                                                    
        )
    print("===========Second Test case: first we create the new user========= ")
    assert response.status_code == 200
    response = client.post(
            "/create_user",
            json={
                "users_name" : "pytest_user2",
                "user_email":  "pytest_user2@agoraflow",
                "password": "TestPassword123",
                "role": "student"
            }
                                                                        
            )
    print("=========== Then we tried creating the duplicate user========= ")
    assert response.status_code == 409
    