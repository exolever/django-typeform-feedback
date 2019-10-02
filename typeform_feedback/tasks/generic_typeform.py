from celery import Task

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from ..models import GenericTypeformFeedback, UserGenericTypeformFeedback
from .mixin import TypeformWebhookMixin


class UpdateGenericTypeformTask(TypeformWebhookMixin, Task):
    name = 'UpdateGenericTypeformTask'
    ignore_result = True

    def get_user(self, response):
        form_response = self._get_form_response(response)
        hidden_fields = self._get_hidden(form_response)
        user_id = hidden_fields.get(
            settings.TYPEFORM_FEEDBACK_WEBHOOK_LABEL_HIDDEN_USER_FIELD,
        )
        return get_user_model().objects.get(pk=user_id)

    def get_object(self, response):
        generic_typeform = None
        form_response = self._get_form_response(response)

        try:
            generic_typeform = GenericTypeformFeedback.objects.get(
                typeform_id=self._get_form_id(form_response)
            )
        except GenericTypeformFeedback.DoesNotExists:
            pass

        return generic_typeform

    def get_object(self, response_from_typeform):
        user_typeform_response = None
        user = self.get_user(response_from_typeform)
        generic_typeform = self.get_object(response_from_typeform)

        if generic_typeform:
            user_typeform_response = UserGenericTypeformFeedback.objects.get_or_create(
                user=user,
                feedback=generic_typeform,
            )

        return user_typeform_response

    def run(self, *args, **kwargs):
        response_from_typeform = kwargs.get('response_from_typeform', {})

        user_typeform_response = self.get_object(response_from_typeform)
        if user_typeform_response:
            user_typeform_response.set_typeform_response(response_from_typeform)