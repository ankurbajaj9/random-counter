# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ../../requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ../../src/user_service.py .
COPY ../../src/common/* ./common/

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the application
CMD ["python", "user_service.py"]