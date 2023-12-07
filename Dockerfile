# Use the official Python 3.11 slim base image
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the local directory (where the Dockerfile is located) to the /app directory inside the container
COPY . /app

# Install Python dependencies from the requirements.txt file, and use --no-cache-dir to avoid caching installation files
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn, a production-ready WSGI server for running Flask applications
RUN pip install gunicorn

# Expose port 5000 to allow external connections to the application
EXPOSE 5000

# Set the entry point command to run Gunicorn with the Flask application
ENTRYPOINT ["gunicorn", "flask_run8:app", "-b", "0.0.0.0:5000"]
