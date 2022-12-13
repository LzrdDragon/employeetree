#!/bin/sh

python /code/treeEmployeeStructure/manage.py migrate
python /code/treeEmployeeStructure/manage.py createcachetable
python /code/treeEmployeeStructure/manage.py collectstatic  --noinput
python /code/treeEmployeeStructure/manage.py initadmin --user=admin --password=admin --force=True

gunicorn --bind 0.0.0.0:8000 --chdir /code/treeEmployeeStructure treeEmployeeStructure.wsgi:application -k gevent --worker-connections 1001 --workers=3

exec "$@"
