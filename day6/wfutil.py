from taskrunner.tasks.foo.task1 import add
from taskrunner.tasks.foo.task2 import mul
from taskrunner.tasks.bar.task1 import div
from taskrunner.tasks.bar.task2 import sub
from taskrunner.celery import app

from celery.result import AsyncResult

import threading

# Define the workflow
Workflow_1 = (div.si(2, 2) | mul.si(4, 4) | add.si(6, 6) | sub.si(8, 8))


# Returns all task objects in a workflow
def nodes(node):
    while node.parent:
        yield node
        node = node.parent
    yield node

# Execute the workflow
result = Workflow_1.apply_async()

# Save the task IDs of the workflow tasks
Workflow_1_tasklist = [task.id for task in nodes(result)]

# Now let's poll the workflow status every 3sec. Ctrl+C to stop
def get_workflow_state():
  threading.Timer(3.0, get_workflow_state).start()
  print("Workflow_1 Status:")
  for task_id in reversed(Workflow_1_tasklist):
      result = AsyncResult(task_id, app=app)
      print({result.id, result.state})

get_workflow_state()
