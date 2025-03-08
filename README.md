# Docker Leanring Projects

This repository contains my leanring journey with Docker. It includes samll assignments and projects that helped me grasp key Docker concepts and practices. The aim is to showcase my understanding of Docker containers, images, volumnes, networks and basic DevOps practices.

Docker images are available - 
    https://hub.docker.com/repositories/vivekbsable


## First Docker File
    1. How to write Docker file.
    2. Sample application to print Hello World.

### Commands: 
    1. docker build -t vivekbsable/first_docker_file:latest .
    2. docker run -it vivekbsable/first_docker_file:latest
    3. docker run -it --entrypoint /bin/bash vivekbsable/first_docker_file:latest

#### Push image to Docker Hub -
    1. docker login
    2. docker push vivekbsable/first_docker_file:latest
