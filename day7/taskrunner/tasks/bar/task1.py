from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='division-of-two-numbers')
def div(args=None, **kwargs):
    time.sleep(5)
    x, y = kwargs['job_data']['div'][0], kwargs['job_data']['div'][1]
    return {'div_result' : x / y}

