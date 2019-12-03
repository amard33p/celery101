from taskrunner.celery import app
import time


@app.task
def mul(x, y):
    time.sleep(5)
    return x * y

