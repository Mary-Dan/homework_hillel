# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
RUN apt-get update && apt-get install -y \
    libpq-dev \
&& rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY messenger_doc /app/messenger_doc

# Install dependencies
COPY messenger_doc/requirements.txt /app/messenger_doc/requirements.txt
RUN pip install --no-cache-dir -r messenger_doc/requirements.txt

# Set the working directory to the Django project directory
WORKDIR /app/messenger_doc

# Expose port 9000 to the outside world
EXPOSE 9000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "messenger.wsgi:application"]

