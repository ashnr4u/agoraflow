# Pytest + FastAPI TestClient — Basic Concepts

## 1. Test Function

We create a function specifically for testing a piece of application behavior.

Pytest identifies functions that follow its test naming convention, such as functions beginning with `test_`.

The test function contains:
- The action we want to test
- The expected result
- An assertion to verify the result

---

## 2. TestClient

FastAPI provides `TestClient` for testing API endpoints.

It allows us to send requests to our FastAPI application from our tests without manually running the API and using a browser or Postman.

Conceptually:
Test → TestClient → FastAPI application → Endpoint

---

## 3. Sending a Request

The test client can send HTTP requests such as:

- GET
- POST
- PUT
- DELETE

For a POST request, we provide:

- The endpoint we want to call
- The JSON data that a real client would send

The endpoint in the test should correspond to an actual endpoint in our FastAPI application.

---

## 4. Response

When the endpoint receives the request, it processes it and returns a response.
The test stores this response so that we can inspect it.
A response can contain things such as:

- HTTP status code
- Response body
- JSON data

---

## 5. Status Code

The HTTP status code tells us what happened with the request.
For example:
- `200` → request succeeded
- `409` → conflict, such as attempting to create something that already exists
The test checks whether the endpoint returned the status code we expected.

---

## 6. Assert

`assert` is used to verify that the actual result matches our expectation.
Conceptually:
Actual result == Expected result
If they match:
> Test passes.
If they don't match:
> Test fails.

---

## 7. Testing User Creation

The user creation test follows this flow:

Create a user  
↓  
Send request to the real user-creation endpoint  
↓  
Receive response  
↓  
Check the status code  
↓  
Verify that user creation succeeded

The purpose is to prove that the endpoint behaves as expected.

---

## 8. Testing Duplicate Email

The duplicate-email test checks application behavior when the same email is used again.

The flow is:

Create the first user  
↓  
Expect successful creation  
↓  
Try creating another user with the same email  
↓  
Expect the API to reject the request  
↓  
Verify the conflict status code

This tests an actual business/integrity rule of the application.

---

## 9. Overall Testing Pattern

Most API tests follow this basic pattern:

Arrange  
↓  
Perform the request  
↓  
Receive the response  
↓  
Assert the expected behavior

The important idea is:

> We are not just checking whether the Python code runs. We are checking whether the real API behaves correctly.

---

## 10. Key Idea

A test should answer:

> "If I perform this real action against my API, do I get the behavior I expect?"

For AgoraFlow, this means using tests to prove that our backend behavior works correctly rather than simply assuming that it works.