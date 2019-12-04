from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='sum-of-two-numbers')
def add(args=None, **kwargs):
    time.sleep(5)
    x = kwargs['mul_result']
    y = kwargs['job_data']['add'][0]
    return {'add_result' : x + y}

