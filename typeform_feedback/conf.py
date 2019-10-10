# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""
# python 3 imports
from __future__ import absolute_import, unicode_literals

# python imports
import logging

# 3rd. libraries imports
from appconf import AppConf

# django imports
from django.conf import settings  # noqa

logger = logging.getLogger(__name__)


class TypeformFeedbackConfig(AppConf):
    DEFAULT_URL = 'https://openexo.typeform.com/to/{}'

    WEBHOOK_LABEL_EVENT_ID = 'event_id'
    WEBHOOK_LABEL_FORM_ID = 'form_id'
    WEBHOOK_LABEL_FORM_RESPONSE = 'form_response'
    WEBHOOK_LABEL_EVENT_TYPE = 'event_type'

    WEBHOOK_DATA_KEYS = [
        WEBHOOK_LABEL_EVENT_ID,
        WEBHOOK_LABEL_FORM_RESPONSE,
        WEBHOOK_LABEL_EVENT_TYPE,
    ]

    WEBHOOK_LABEL_HIDDEN = 'hidden'
    WEBHOOK_LABEL_HIDDEN_USER_FIELD = 'user_id'
    WEBHOOK_LABEL_CALCULATED = 'calculated'
    WEBHOOK_LABEL_SCORE = 'score'
    WEBHOOK_LABEL_CONTENT_TYPE = 'content_type_id'
    WEBHOOK_LABEL_OBJECT_ID = 'object_id'

    WEBHOOK_REMOTE_ALLOWED_IP = [
        '107.22.86.211',
        '23.22.56.151',
        '54.204.242.155',
    ]

    CH_WEEKLY = 'S'

    TYPE_CHOICES = (
        (CH_WEEKLY, 'Weekly'),
    )

    USER_FEEDBACK_STATUS_NONE = 'N'
    USER_FEEDBACK_STATUS_PENDING = 'P'
    USER_FEEDBACK_STATUS_ANSWERED = 'A'
    USER_FEEDBACK_STATUS_DONE = 'D'
    USER_FEEDBACK_STATUS_FAIL = 'F'
    USER_FEEDBACK_STATUS_DEFAULT = USER_FEEDBACK_STATUS_PENDING

    USER_FEEDBACK_STATUS_CHOICES = (
        (USER_FEEDBACK_STATUS_NONE, 'Not available'),
        (USER_FEEDBACK_STATUS_PENDING, 'Pending'),
        (USER_FEEDBACK_STATUS_ANSWERED, 'Answered'),
        (USER_FEEDBACK_STATUS_DONE, 'Done'),
        (USER_FEEDBACK_STATUS_FAIL, 'Fail'),
    )

