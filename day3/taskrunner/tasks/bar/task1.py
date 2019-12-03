from taskrunner.celery import app
import time


@app.task
def div(x, y):
    time.sleep(5)
    return x / y

