from celery import Celery

APP_NAME = 'taskrunner'

app = Celery(APP_NAME,
             broker='amqp://',
             backend='redis://localhost:6379/0',
             include=['{}.tasks'.format(APP_NAME)])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    # https://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_track_started
    task_track_started=True,
)

if __name__ == '__main__':
    app.start()
