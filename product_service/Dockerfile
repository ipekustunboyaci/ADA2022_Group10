# Using python 3.9 full image as the base image
FROM python:3.9.7-slim
# Working directory
WORKDIR /code
# Copy requirements.txt  to the working directory
COPY ./requirements.txt /code/requirements.txt
# Install required python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Copy all files in app folder
COPY ./app /code/app


