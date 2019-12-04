from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='diff-of-two-numbers')
def sub(args=None, **kwargs):
    time.sleep(5)
    x = kwargs['add_result']
    y = kwargs['job_data']['sub'][0]
    return {'sub_result' : x - y}

