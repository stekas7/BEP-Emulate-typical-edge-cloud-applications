# Use an official Python runtime as the parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install kafka-python dependency
RUN pip install --no-cache-dir kafka-python

# Install requests
RUN pip install requests

RUN pip install matplotlib

# Run kafkascript.py when the container launches
CMD ["python", "./kafkascript.py"]
