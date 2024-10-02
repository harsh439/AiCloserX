from celery import Celery

# Celery instance
celery_app = Celery('app', broker='redis://localhost:6379/0')

# Load custom configurations if needed
celery_app.conf.update(
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    enable_utc=True,
    timezone='UTC',
)

# Discover and register tasks from 'tasks.py'
celery_app.autodiscover_tasks(['app.core.tasks'])
