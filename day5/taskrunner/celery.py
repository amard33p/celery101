from celery import Celery

import os
import sys

sys.path.insert(0, os.getcwd())


APP_NAME = 'taskrunner'

task_root = os.path.join(APP_NAME, 'tasks')

def taskDetector(task_root):
    tasks = []
    for root, dirs, files in os.walk(task_root):
        for filename in files:
            if filename != '__init__.py' and filename.endswith('.py'):
                task = os.path.join(root, filename)\
                    .replace('/', '.')\
                    .replace('.py', '')
                tasks.append(task)
    return tasks

app = Celery(APP_NAME,
             broker='amqp://',
             backend='redis://localhost:6379/0',
             include=taskDetector(task_root))

app.conf.update(
    result_expires=3600,
    task_track_started=True,
)

if __name__ == '__main__':
    app.start()
