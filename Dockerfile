# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 5000
EXPOSE 5000

# Default command (Use python -m django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]

