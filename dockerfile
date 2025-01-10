# Use the official Python image from the Docker Hub.
FROM python:3.9

# Set the working directory in the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install any necessary packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files.
RUN python manage.py collectstatic --noinput

# Expose port 8000, the default port used by Django.
EXPOSE 8000

# Run the Django application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
