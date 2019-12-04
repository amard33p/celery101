# How to Dockerize a Celery App With Django REST Framework And RabbitMQ

Example taken from - https://github.com/xlwings/python-celery-dockerize-celery-django  

1. Bring up the docker stack:
   `docker-compose up -d`

2. Rest API is available on http://localhost:8000

3. Trigger a workflow:
   `curl -d 'testcase=ESG-TC01' -d 'job_data={"div" : [4, 2], "mul" : [3], "add" : [6], "sub" : [2]}' -X POST http://localhost:8000`  
   This will return a list of task ids.

4. Use the list to get workflow status:
   `curl -d 'task_list=["e2f970f6-52ed-48fe-ad4c-93c31d312f92","303c37f8-f079-4bc7-a0b4-b311c6fdb65e"]' -X GET http://localhost:8000`

5. Monitor tasks in flower:
   [http://localhost:5555](http://localhost:5555)
