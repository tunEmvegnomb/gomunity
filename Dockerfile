# FROM python:3.8-alpine
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# RUN apk update
# RUN apk add build-base python3-dev py-pip jpeg-dev zlib-dev libpq-dev
# # RUN apk --no-cache add build-base python3-dev py-pip jpeg-dev zlib-dev libpq-dev gcc gfortran musl-dev linux-headers g++ libffi-dev openssl-dev

# COPY requirements.txt /usr/src/app/

# WORKDIR /usr/src/app
# RUN pip install -r requirements.txt

# COPY . /usr/src/app/

FROM python:3.8-buster
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
RUN apt-get update -y 
RUN apt-get upgrade -y 
RUN apt-get install -y ffmpeg libgl1-mesa-glx COPY requirements.txt /usr/src/app/ 
WORKDIR /usr/src/app RUN pip install -r requirements.txt COPY . /usr/src/app/


# FROM python:3.9.10-buster
# ENV PYTHONDONTWRITEBYTECODE=1 
# ENV PYTHONUNBUFFERED=1 
# RUN apt-get update -y 
# RUN apt-get upgrade -y 
# RUN apt-get install -y ffmpeg libgl1-mesa-glx COPY requirements.txt /usr/src/app/ 
# WORKDIR /usr/src/app RUN pip install -r requirements.txt COPY . /usr/src/app/