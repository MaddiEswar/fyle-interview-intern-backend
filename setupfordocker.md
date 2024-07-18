1. Create a Dockerfile:


FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]


2. Create a docker-compose.yml:

version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development


3. Document build and run instructions:

# Docker Setup

## Build the Docker image
```sh
docker build -t flye_assignment .

4. Run the Docker container

docker run -p 5000:5000 flye_assignment

5. Using docker-compose

docker-compose up --build

