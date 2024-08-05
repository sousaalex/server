FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY server.py server.py
COPY .env .env

EXPOSE 8765

CMD ["python3", "server.py"]
