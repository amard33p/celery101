from taskrunner.tasks.foo.task1 import add
from taskrunner.tasks.foo.task2 import mul
from taskrunner.tasks.bar.task1 import div
from taskrunner.tasks.bar.task2 import sub

from celery import group


# Serial workflow with dependent tasks
# ************

# 4 / 2 * 3 + 6 - 2
#workflow = (div.s(4, 2) | mul.s(3) | add.s(6) | sub.s(2)).apply_async()
# OR
workflow1 = (div.s(4, 2) | mul.s(3) | add.s(6) | sub.s(2))()
print(workflow1.get())


# Serial workflow with independent tasks
# ************

#workflow2 = (div.si(2, 2) | mul.si(4, 4) | add.si(3, 2) | sub.si(8, 8))()
#print(workflow2.get())
#print(workflow2.parent.get())
#print(workflow2.parent.parent.get())
#print(workflow2.parent.parent.parent.get())


# Parallel workflow
# ************

#workflow3 = group(div.s(2, 2) , mul.s(4, 4) , add.s(3, 2) , sub.s(8, 8))()
#print(workflow3.get())


# Diamond workflow
# ************

#             x = mul(3, 2)
#            /             \
# div(4, 2)--               --sub(x, y)
#            \             /
#             y = add(1, 2)

#workflow4 = (div.si(4, 2) | group(mul.si(3, 2), add.si(1, 2)) | sub.s())()
#print(workflow4.get())
