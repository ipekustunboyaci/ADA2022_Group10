# Using python 3.7 full image as the base image
FROM python:3.7-slim-buster
# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in courierservice host directory to /usr/src/myapp in Docker container
COPY . .