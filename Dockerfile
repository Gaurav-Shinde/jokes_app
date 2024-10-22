# Use a minimal base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt if you have it, otherwise we will install packages directly
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]