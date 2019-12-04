from taskrunner.tasks.foo.task1 import add
from taskrunner.tasks.foo.task2 import mul
from taskrunner.tasks.bar.task1 import div
from taskrunner.tasks.bar.task2 import sub

from celery import chain
from celery.result import AsyncResult

from taskrunner.celery import app

# Workflow tasklist definition
RunTC01Workflow = [div, mul, add, sub]
RunTC02Workflow = [div, mul]
RunTC03Workflow = [add, sub]

# Testcase name to workflow mapping
TESTCASE_WORKFLOWS = {
'ESG-TC01': RunTC01Workflow,
'ESG-TC02': RunTC01Workflow,
'ESG-TC03': RunTC01Workflow,
}

# Workflow generator
def run_workflow(testcase, job_data):
    task_list = TESTCASE_WORKFLOWS[testcase]
    _tasks = tuple(getattr(task, 's')(job_data = job_data) for task in task_list)
    wf_result =  chain(*_tasks).apply_async()
    wf_task_id_list = [task.id for task in nodes(wf_result)]
    return reversed(wf_task_id_list)

# Traverse chain using child task ID
def nodes(node):
    while node.parent:
        yield node
        node = node.parent
    yield node

def get_task_status(task_id):
    _result = AsyncResult(task_id, app=app)
    return _result.state

def get_wf_status(task_list):
    wf_status_dict = {task_id: get_task_status(task_id) for task_id in task_list}
    return wf_status_dict
