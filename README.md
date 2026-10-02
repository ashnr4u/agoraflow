# AgoraFlow

A backend engineering project for managing college events and student registrations.

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Redis
* JWT
* Docker

## Current Progress

* PostgreSQL running with Docker Compose
* Persistent database volume configured
* Database connection verified
* Alembic configured for database migrations
* User creation API implemented
* Event creation API implemented
* Event listing API implemented with Pydantic response models
* Event listing supports query-based result limiting
* Student registration API implemented
* JWT authentication implemented
* Role-based access control (RBAC) implemented for students and organisers
* Idempotent registration implemented using Redis
* Atomic Redis `SET NX` used to handle duplicate requests
* Race conditions in the registration flow reproduced and handled

## Goal

Build a production-oriented backend while learning and implementing concepts such as:

* REST APIs
* Authentication and authorization
* Database design and constraints
* Idempotency
* Concurrency and race conditions
* Redis
* Caching and rate limiting
* Background jobs
* Testing
* Failure handling
* Production deployment
