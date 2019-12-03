from taskrunner.celery import app
from taskrunner.tasks.baseTask import CustomBaseTask

import time


@app.task(base=CustomBaseTask, name='product-of-two-numbers')
def mul(args=None, **kwargs):
    time.sleep(5)
    x = kwargs['div_result']
    y = kwargs['job_data']['mul'][0]
    return {'mul_result' : x * y}

