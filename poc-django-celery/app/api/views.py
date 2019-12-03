import logging
import json

from rest_framework.response import Response
from rest_framework.views import APIView

from api import wfutil


logger = logging.getLogger(__name__)


class MyView(APIView):
    
    def get(self, request, format=None):
        task_list = request.POST.get('task_list')
        return Response(wfutil.get_wf_status(json.loads(task_list)))

    def post(self, request):
        testcase = request.POST.get('testcase')
        job_data = json.loads(request.POST.get('job_data'))
        task_ids = wfutil.run_workflow(testcase, job_data)
        return Response(task_ids)

