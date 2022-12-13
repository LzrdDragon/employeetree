FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/requirements_unix.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

RUN chmod +x ./code/entrypoint.sh

WORKDIR /code/treeEmployeeStrucure
