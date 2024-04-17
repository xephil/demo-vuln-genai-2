#FROM python:slim
FROM cgr.dev/chainguard/python:latest-dev

WORKDIR /app

COPY requirements.txt /app

# Install packages from requirements.txt,
# then install langchain-community
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install -U psutil

# Make sure the entire project directory is copied
COPY . /app

CMD ["app.py"]
