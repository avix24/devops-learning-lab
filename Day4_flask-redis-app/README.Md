```markdown
# Day 4 - Flask + Redis App using Docker Compose

## Objective
Create a Python Flask application connected to Redis to track page visits, using Docker Compose to manage multiple containers.

## Steps to Run
1. Navigate to the folder: `cd Day4_flask-redis-app`
2. Build and start containers:
   ```bash
   docker-compose up --build -d
3. Open your browser and go to http://localhost:8080
4. Refresh the page to see the visit count increment.

## What I Learned

- Linking multiple containers using Docker Compose.
- Exposing ports and networking between services.
- Debugging real container communication issues (like Redis connection)
- Handling errors in Flask and Redis integration.
