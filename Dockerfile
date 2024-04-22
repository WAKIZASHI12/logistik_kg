FROM python:3.12.3

WORKDIR /app

RUN apt update -y && apt upgrade -y
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./
