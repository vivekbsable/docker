# Use Python base image.
FROM python:3.9

# Set default environemnt variable.
ENV IMAGE_NAME="vivekbsable/container_with_arguments"
ENV MY_DOCKERFILE_ENV_01="Hello from Dockerfile environment variable 01"
ENV MY_DOCKERFILE_ENV_02="Hello from Dockerfile environemnt variable 02 which we are overwriting."

# Copy the Python script into the container.
COPY app.py /app/app.py

# Set working directory in image.
WORKDIR /app

# Run to start the script.
ENTRYPOINT ["python", "app.py"]
# This Command will overwrite only if you not provided anything in run command.
# If you want to make it dynamic then need to add script which will add missing arguments.
CMD ["10", "20", "-name", "Vivek", "--surname", "Sable"]
