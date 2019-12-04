"""taskrunner.py

Usage::

   (window1)$ python taskrunner.py worker -l info

   (window2)$ python
   >>> from taskrunner import add
   >>> add.delay(16, 16).get()
   32


You can also specify the app to use with the `celery` command,
using the `-A` / `--app` option::

    $ celery -A taskrunner worker -l info

"""


import time

from celery import Celery

app = Celery(
    'taskrunner',
    broker='amqp://',
    backend='rpc'
)


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


if __name__ == '__main__':
    app.start()