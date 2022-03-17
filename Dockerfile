FROM python:3.8-slim-buster
WORKDIR /lab1
COPY . .
CMD ["python","main.py"]
