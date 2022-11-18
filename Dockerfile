FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code


RUN python3 treeEmployeeStructure/manage.py collectstatic --noinput


EXPOSE 8000

ENTRYPOINT ["python", "treeEmployeeStructure/manage.py"]
CMD ["runserver", "127.0.0.1:8000"]
