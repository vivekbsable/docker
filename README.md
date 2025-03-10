# Docker Leanring Projects

This repository contains my leanring journey with Docker. It includes samll assignments and projects that helped me grasp key Docker concepts and practices. The aim is to showcase my understanding of Docker containers, images, volumnes, networks and basic DevOps practices.

Docker images are available - 
    https://hub.docker.com/repositories/vivekbsable


## 1. First Docker File
    1. How to write Docker file.
    2. Sample application to print Hello World.

### Commands: 
    1. docker build -t vivekbsable/first_docker_file:latest .
    2. docker run -it vivekbsable/first_docker_file:latest
    3. docker run -it --entrypoint /bin/bash vivekbsable/first_docker_file:latest

#### Push image to Docker Hub -
    1. docker login
    2. docker push vivekbsable/first_docker_file:latest

## 2. Web application deploy with Docker
    Use Django to create proejct and application to run web aaplication on docker container.
Only single API is added inside application.

### How Port Mapping Works
Containers run in isolated environments, meaning they don’t expose their internal ports to the host by default. The -p option allows traffic from the host machine to reach the container.

#### For example:
In this example, Django app inside the container is running on port 8000, then:
Without -p 8000:8000, you cannot access it from your host machine.
With -p 8000:8000, you can access it by visiting http://localhost:8000 on your browser.
