# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import JSONField

from model_utils.models import TimeStampedModel

from ..conf import settings


class UserGenericTypeformFeedback(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )
    feedback = models.ForeignKey(
        'GenericTypeformFeedback',
        null=False, blank=False,
        related_name='responses',
        on_delete=models.CASCADE,
    )
    _response = JSONField(
        default=[],
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=1,
        blank=False, null=False,
        choices=settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_CHOICES,
    )

    def __str__(self):
        return '{} - {}'.format(
            self.user, self.feedback,
        )

    def get_project(self):
        return self.feedback.related_to.first().project

    @property
    def url(self):
        return self.feedback.url

    @property
    def response(self):
        return self.first_response

    @property
    def responses(self):
        return self._response

    @property
    def first_response(self):
        return self._response[0] if len(self._response) > 0 else {}

    @property
    def last_response(self):
        return self._response[-1] if len(self._response) > 0 else {}

    def set_typeform_response(self, response):
        self._response.append(response)
        self.status = settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_DONE
        self.save(update_fields=['_response', 'status', 'modified'])
