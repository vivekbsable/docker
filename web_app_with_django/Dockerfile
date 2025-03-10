# Base image name
FROM ubuntu:latest

WORKDIR /app

# Copy requirement.txt container.
COPY requirements.txt /app
# Copy code into docker container.
COPY web_app /app/web_app

RUN apt-get update && \ 
    apt-get install -y python3 python3-pip python3-venv

# Set detault shell from sh to bash.
#  This is useful when you want to use Bash-specific syntax in
#  Dockerfile commands instead of the default shell (sh).
SHELL ["/bin/bash", "-c"]
# Virtual Environement because
#   WARNING: Running pip as the 'root' user can result in broken permissions
#   and conflicting behaviour with the system package manager.
#   It is recommended to use a virtual environment instead.
WORKDIR /app/web_app

RUN python3 -m venv venv1 && \
    source venv1/bin/activate && \
    pip install --no-cache-dir -r /app/requirements.txt

# --no-cache-dir
# Normally, pip caches downaload .whl, .tar.gz files in ~/.cache/pip/.
# This option prevent them to store on container.

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD source venv1/bin/activate && python3 manage.py runserver 0.0.0.0:8000
# Instead of using source venv1/bin/activate, 
#  we directly call the Python interpreter from venv1/bin/python,
#  which ensures it uses the virtual environment.
CMD ["venv1/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]