# Day 3 - Nginx Docker Hands-On

## Objective
Learn to containerize a simple Nginx web server using Docker.

## Steps to Run
1. Navigate to the folder: `cd Day3_Nginx`
2. Build the Docker image (if Dockerfile is present):

Command:
- docker build -t my-nginx .

3. Run the container:
Command:
- docker run -d -p 8080:80 my-nginx

4. Open your browser and go to http://localhost:8080

## What I Learned:
													 
- Basics of Dockerfile and building images.
- Running a container with port mapping.
- Accessing the containerized application via browser.
