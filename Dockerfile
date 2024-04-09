FROM python:slim

WORKDIR /app

# Update system packages and install any needed dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends && \
    RUN apt-get install -y libexpat1=2.5.0-1 && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app

# Install packages from requirements.txt,
# then install langchain-community
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install -U psutil

# Make sure the entire project directory is copied
COPY . /app

CMD ["python", "app.py"]
