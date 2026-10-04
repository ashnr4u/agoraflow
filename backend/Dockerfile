FROM python:3.12-slim
# Start with a Python base image; the container needs its own Python environment.

WORKDIR /backend
# Set the container's working directory; paths below are relative to this location.

COPY requirements.txt .
# Copy dependencies first so Docker can install them inside the container.

RUN pip install -r requirements.txt
# Install the project's dependencies inside the container.

COPY src /backend/src
# Copy the actual project code; COPY needs both source and destination.