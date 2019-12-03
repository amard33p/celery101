from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='diff-of-two-numbers')
def sub(x, y):
    time.sleep(5)
    return x - y

