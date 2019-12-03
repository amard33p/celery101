## Passing arguments to a workflow?

* Let's consider a real world example where a workflow would consist of a serial chain of tasks with data being shared between them.  
  `Workflow_1 = (div.s(4, 2) | mul.s(3) | add.s(6) | sub.s(2))`
* However the task arguments will be fed at runtime.  
* For example, this job_data needs to be available to all tasks:  
  `job_data = {'div' : [4, 2], 'mul' : [3], 'add' : [6], 'sub' : [2]}`
* Now `apply_async` accepts args and kwargs but this will only be applied to the first task in the chain.
* So instead we will pass the arguments as kwargs to the task signatures and modify our workflow definition thus:
  ```
  def Workflow_1(job_data):
    return (div.s(job_data = job_data) | mul.s(job_data = job_data)| add.s(job_data = job_data)| sub.s(job_data = job_data))
  
  # A neater way
  from taskrunner.tasks.foo.task1 import add
  from taskrunner.tasks.foo.task2 import mul
  from taskrunner.tasks.bar.task1 import div
  from taskrunner.tasks.bar.task2 import sub

  from celery import chain

  job_data = {'div' : [4, 2], 'mul' : [3], 'add' : [6], 'sub' : [2]}
  
  def workflow_generator(task_list):
      result = tuple(getattr(task, 's')(job_data = job_data) for task in task_list)
      return chain(*result)
  
  Workflow_1 = workflow_generator([div, mul, add, sub]) 
  ```
* Now we need to modify our tasks to accept the arguments.  
  ```
  @app.task(base=CustomBaseTask, name='division-of-two-numbers')
  def div(*args, **kwargs):
      time.sleep(5)
      x, y = kwargs['job_data']['div'][0], kwargs['job_data']['div'][1]
      return x / y
  
  @app.task(base=CustomBaseTask, name='product-of-two-numbers')
  def mul(*args, **kwargs):
      time.sleep(5)
      x = args[0] # return from div()
      y = kwargs['job_data']['mul'][0]
      return x * y
  ```
* It would be better if the tasks could look for kwargs only but in a chain the return value of a task is sent only as args to the next task.  
  To overcome this, we can add logic in our [BaseTask class][1] which checks if args[0] contains a dict and if true, moves it to kwargs.
  ```
  def __call__(self, *args, **kwargs):
  if len(args) == 1 and isinstance(args[0], dict):
      kwargs.update(args[0])
      args = ()
      return self.run(*args, **kwargs)
  ```
* Now we can change our tasks to accept args=None and **kwargs. To completely remove specifying args=None, we may use [Celery-Signals][2]
 

[1]: day7/taskrunner/tasks/baseTask.py#10-13
[2]: https://docs.celeryproject.org/en/latest/userguide/signals.html


