# Параметр CELERY_ALWAYS_EAGER позволяет выполнять задачи локально на синхронной основе, а не отправлять их в очередь.
from .celery import app as celery_app