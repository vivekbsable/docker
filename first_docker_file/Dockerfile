# Base image from public registry.
FROM ubuntu:latest

# Set working directory in image.
WORKDIR /app

# Copy files from host file system to image file system.
COPY . /app/

# Install neccessary packages.
RUN apt-get update && apt-get install -y python3 python3-pip

# Set Environment Variabls.
ENV IMAGE_NAME="vivekbsable/first_docker_file"

# Run/entrypoint to start the application.
CMD ["python3", "/app/app.py"]