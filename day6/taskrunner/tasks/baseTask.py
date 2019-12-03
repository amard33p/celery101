import celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

class CustomBaseTask(celery.Task):
    name = 'CustomBaseTaskClass'
    description = ''

    def __call__(self, *args, **kwargs):
        logger.info("Starting to run")
        logger.info('Task-{0!r} with id-{1!r} STARTED with args={2!r} and kwargs={3!r} '.format(self.name, self.request.id, args, kwargs))
        return self.run(*args, **kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        logger.info("Ending run")
        pass

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('Task-{0!r} with id-{1!r} SUCCEEDED'.format(self.name, task_id))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.info('Task-{0!r} with id-{1!r} FAILED with err-{2!r}'.format(self.name, task_id, exc))

