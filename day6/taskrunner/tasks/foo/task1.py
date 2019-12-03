from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='sum-of-two-numbers')
def add(x, y):
    time.sleep(5)
    return x + y

