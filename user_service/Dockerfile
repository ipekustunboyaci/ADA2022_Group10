# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /code
# Copy requirements.txt  to the working directory
COPY ./requirements.txt /code/requirements.txt
# Install required python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Copy all files in app folder
COPY ./app /code/app