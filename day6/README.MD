## How to get the status of a workflow?

* Let's consider a workflow of serial tasks.  
  `Workflow_1 = (div.si(2, 2) | mul.si(4, 4) | add.si(6, 6) | sub.si(8, 8))`
* On running the workflow, the result object will reference the last task in the chain.
  We need to traverse up the chain using a generator to access all tasks in the
  workflow.
  ```
  def nodes(node):
    while node.parent:
        yield node
        node = node.parent
    yield node

  result = Workflow_1.apply_async()
  Workflow_1_tasklist = [task.id for task in nodes(result)]
  ```
* Now this tasklist can be saved to a db. Note that the list is in reversed order.
* Even the tasks themselves can provide task info through the BaseClass [\__call__][1] method.
* An important difference between two approaches is that the `result` object cannot access `task.name`. 
  This info can only be accessed within the tasks themselves.
* To query the workflow status, we first retrieve the tasklist, create an `AsyncResult` object using the task_ids,
  and then query its state.
  ```
  for task_id in reversed(Workflow_1_tasklist):
      result = AsyncResult(task_id, app=app)
      print({result.id, result.state})
  ```

### Using Flower

* `pip install flower`
* Open a new terminal and run `flower -A taskrunner --broker=amqp://guest:guest@localhost:5672//`
* `curl -X GET http://localhost:5555/api/task/info/TASK_ID`
  ```
  {
    "uuid": "035504e5-89d6-43f4-bc8a-b5e0588be14d",
    "name": "diff-of-two-numbers",
    "state": "SUCCESS",
    "received": 1574678654.7077875,
    "sent": null,
    "started": 1574678654.7103007,
    "rejected": null,
    "succeeded": 1574678659.7206867,
    "failed": null,
    "retried": null,
    "revoked": null,
    "args": "[8, 8]",
    "kwargs": "{}",
    "eta": null,
    "expires": null,
    "retries": 0,
    "worker": "celery@ub18-dev-amar-01",
    "result": "0",
    "exception": null,
    "timestamp": 1574678659.7206867,
    "runtime": 5.009667221456766,
    "traceback": null,
    "exchange": null,
    "routing_key": null,
    "clock": 797,
    "client": null,
    "root": "31a9d888-6426-4034-96d7-b31a7a7a5a76",
    "root_id": "31a9d888-6426-4034-96d7-b31a7a7a5a76",
    "parent": "7f69b88f-7531-4e0f-b02d-5931fc2b3588",
    "parent_id": "7f69b88f-7531-4e0f-b02d-5931fc2b3588",
    "children": []
  }
  ```
 

[1]: day6/taskrunner/tasks/baseTask.py#12


