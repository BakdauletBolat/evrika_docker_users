FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/