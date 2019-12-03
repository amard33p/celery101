from taskrunner.tasks.foo.task1 import add
from taskrunner.tasks.foo.task2 import mul
from taskrunner.tasks.bar.task1 import div
from taskrunner.tasks.bar.task2 import sub
from taskrunner.celery import app

from celery import chain
from celery.result import AsyncResult

import threading


# The Job data
job_data = {'div' : [4, 2], 'mul' : [3], 'add' : [6], 'sub' : [2]}

# Workflow generator template
def workflow_generator(task_list):
    result = tuple(getattr(task, 's')(job_data = job_data) for task in task_list)
    return chain(*result)


# Defining the workflow
Workflow_1 = workflow_generator([div, mul, add, sub])

# Run the workflow
result = Workflow_1.apply_async()

# Returns all task objects in a workflow
def nodes(node):
    while node.parent:
        yield node
        node = node.parent
    yield node

# Save the task IDs of the workflow tasks
Workflow_1_tasklist = [task.id for task in nodes(result)]
print(Workflow_1_tasklist)

# Now let's poll the workflow status every 3sec. Ctrl+C to stop
def get_workflow_state():
  threading.Timer(3.0, get_workflow_state).start()
  print("Workflow_1 Status:")
  for task_id in reversed(Workflow_1_tasklist):
      result = AsyncResult(task_id, app=app)
      print({result.id, result.state})

get_workflow_state()
