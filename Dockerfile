FROM python:3.8

WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt /app

# Install packages from requirements.txt,
# then install langchain-community
RUN pip install -r requirements.txt && \
    pip install -U psutil

# Make sure the entire project directory is copied
COPY . /app

CMD ["python", "app.py"]
