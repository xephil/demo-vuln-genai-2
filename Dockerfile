#FROM python:slim
FROM cgr.dev/chainguard/python:latest-dev

USER root

WORKDIR /app

COPY requirements.txt /app

# Install Python packages specified in requirements.txt
# and additional package psutil
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install -U psutil

# Make sure the entire project directory is copied
COPY . /app

CMD ["app.py"]
