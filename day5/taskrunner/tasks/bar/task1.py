from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='division-of-two-numbers')
def div(x, y):
    time.sleep(5)
    return x / y

