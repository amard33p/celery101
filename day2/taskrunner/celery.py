from celery import Celery

APP_NAME = 'taskrunner'

app = Celery(APP_NAME,
             broker='amqp://',
             backend='redis://localhost:6379/0',
             include=['{}.task1'.format(APP_NAME), '{}.task2'.format(APP_NAME)])

app.conf.update(
    result_expires=3600,
    task_track_started=True,
)

if __name__ == '__main__':
    app.start()
