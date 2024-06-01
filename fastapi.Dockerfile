# syntax=docker/dockerfile:1
# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the container
COPY . /app

# Expose the port FastAPI will run on
EXPOSE 8001
# Run the application
CMD ["poetry", "run", "uvicorn", "fast-api.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
