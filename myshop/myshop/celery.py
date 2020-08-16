import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
# app.conf.update(
#     CELERY_ALWAYS_EAGER=True,
# )
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#######################
##-Terminal->Local(2)-------
#celery -A myshop worker --loglevel=INFO --concurrency=10 -n worker1.%h
##сообщение-mail прилетает после ctrl-c, а в консоли celery ничего нет???????
###########
##flower: надо уст. с https://github.com/mher/flower/zipball/master#egg=flower
