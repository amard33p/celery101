from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(name='product-of-two-numbers')
def mul(x, y):
    time.sleep(5)
    return x * y

