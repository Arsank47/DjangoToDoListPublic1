# Use the official Python image based on Alpine
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev bash

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project, including the todo_list directory
COPY . .

# Ensure SQLite database persistence
VOLUME /app/db.sqlite3

# Set the working directory to the todo_list directory
WORKDIR /app/todo_list

# Expose the port the app runs on
EXPOSE 8003

# Command to run the application with migrations
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8003"]
