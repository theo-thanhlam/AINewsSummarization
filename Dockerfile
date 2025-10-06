FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
ENV PYTHONPATH=":/app"
# Install dependencies (if requirements.txt exists)
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the whole project into container
COPY . .

# Default command to run your script
# CMD ["python3", "main.py"]