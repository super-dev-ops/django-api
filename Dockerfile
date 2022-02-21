FROM ubuntu:20.04

# LABEL about the custom image
LABEL maintainer="supriya-sontakke@hotmail.com"
LABEL version="0.1"
LABEL description="This is custom Docker Image created with GitHub actions and contains Django project"


# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository
RUN apt update; mkdir -p /src; mkdir -p /src/files

RUN apt install postgresql-client  -y
RUN apt install python3 -y
RUN apt install python3-pip -y
#RUN apt install postgresql postgresql-contrib

COPY requirements.txt /src/files/requirements.txt
RUN pip install -r /src/files/requirements.txt
COPY . /src
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
# Expose Port for the Application 
EXPOSE 8080

CMD python3 /src/manage.py runserver 0.0.0.0:8080