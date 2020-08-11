# python-celery-flask-example

Python 3.7 compatible.

Sample code to run a Flask App with Celery workers and period tasks.

Execute `run.sh`.

This will start Redis in docker, and python apps for celery worker, celery beat and flask.

You can run this in a virtual env

## Flask

Single endpoint on `/` that returns `10` as a result of executing a Celery task.
This task is `add_together()` defined within `app.py`.

## Celery

Celery is instantiated in `tasks.py` . the actual tasks are defined in `app.py` and can be defined in any module.

### Task triggered with Flask

`add_together` task is executed everytime the `/` endpoint is called with `GET` method. This demonstrates that celery 
task can be executed. See [this guide](https://flask.palletsprojects.com/en/1.1.x/patterns/celery/)

### Periodic/scheduled task

The task `repetitive_task` is scheduled to run on a cron schedule of every 1 minute. This task runs regardless of Flask 
API being invoked. This requires `celery beat` to run. 
See [this guide](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#starting-the-scheduler). 
