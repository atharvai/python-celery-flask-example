from celery.schedules import crontab
from flask import Flask

from datetime import datetime

from tasks import make_celery

flask_app = Flask('app')
"""
running flask with celery workers https://flask.palletsprojects.com/en/1.1.x/patterns/celery/
"""
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celery = make_celery(flask_app)


@celery.task()
def add_together(a, b):
    print(str(a+b))
    return a + b

@celery.task()
def repetitive_task():
    """
    simple task to be executed on a schedule
    :return:
    """
    print('period task executed' + datetime.utcnow().isoformat())

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Scheduled Tasks: https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#starting-the-scheduler
    :param sender:
    :param kwargs:
    :return:
    """
    sender.add_periodic_task(crontab(), repetitive_task.s(),name='scheduled_task')


@flask_app.route('/')
def home():
    result = add_together.delay(5, 5)
    return str(result.wait())


if __name__ == '__main__':
    flask_app.run()
