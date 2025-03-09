# Base image
FROM ubuntu:latest

# Install Python3 package.
RUN apt-get update && apt-get install -y python3 python3-pip

# Verify installation.
RUN python3 --version

CMD ["python3", "--version"]
