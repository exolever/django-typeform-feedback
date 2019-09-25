from celery import Task

from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from .tasks import TypeformWebhookMixin


class UpdateGenericTypeformTask(TypeformWebhookMixin, Task):
    name = 'UpdateGenericTypeformTask'
    ignore_result = True

    pass
