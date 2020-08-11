#!/usr/bin/env bash


#run redis for celery backend
docker run --rm -p 6379:6379 --name example_redis -dt redis:latest

# run flask app
python app.py & flask_app_pid=$!

# run celery beat
celery -A app.celery beat & celery_beat_pid=$!

# run celery worker
celery -A app.celery worker

docker stop example_redis &&\
kill -0 "$flask_app_pid" &&\
kill -0 "$celery_beat_pid" || true
