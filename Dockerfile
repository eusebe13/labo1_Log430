FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer ruff
RUN pip install --no-cache-dir ruff

COPY app/ .

CMD ["python", "app/main.py"]
