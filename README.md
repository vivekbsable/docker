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


## 3. How to pass and use arguments in Container
We can pass parameters to a Docker container in multiple ways and access in your code(Python)

### Pass as Command-Line Arguments
I can pass parameters as arguments when running the container and read them using sys.argv in Python.
In Docker, both `CMD` and `ENTRYPOINT` define how a container runs.
However, wheb passing positional arguments, ENTRYPOINT is preferred because it ensure all arguments are treated as part of the command execution.

### Pass as Environemnt Variable
Use `-e` to pass environment variable when runiing the container

### Use Dockerfile ENV Veraibles
I can define default environemnt veraible in a Dockerfile.

    ENV IMAGE_NAME="vivekbsable/container_with_arguments"

### Command
1. Positional Arguments: `10 20`
2. Keyword Arguments: `name, surname`
3. Envrionemnt Variable: `SCRIPT_LANG, MY_DOCKERFILE_ENV_02`

    docker run -it -e SCRIPT_LANG="Python" -e MY_DOCKERFILE_ENV_02="Overwrite by command line" -t vivekbsable/container_with_arguments:latest 10 20 --name Vivek --surname Sable


## 4. Docker Bind Mounts
Container file system is not not persistent. Container can not read or load file on host operating file system.
Mounting folder from container to host machine. Both folders are synch together.
We can attach same mount directory with other container.


### Comnands

Mount the ./data/directory from your local machine to /data inside the container.

    docker run -v src:dest -t <image_name>
    docker run -v $(pwd)/data/logs:/app/data/logs -t <image_name>

Anything is crrated on local or container mount directories, will be synch to eachother.


## 5. Docker Volume
Volums are completely manged by Docker.
We can manage lifecycle of Volumes.

### List the volumes (Driver, Volume Name)

    docker volume ls

### Create Volume
Create logical partition on file system which we can not see direclty.

    docker volume create <volume_name>

### Details of volume

    docker volume inspect <volume_name>

Check Driver, Moutpoint and name.

### Delete Volume

    docker volume rm <volume_name>


### Docker run

    docker run -it -v <volume_name>:<target dir> -t <image_name>

    docker volume create app_test
    docker run -it -v app_test:/app/data/logs -t <image_name>
