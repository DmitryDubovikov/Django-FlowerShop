FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app 