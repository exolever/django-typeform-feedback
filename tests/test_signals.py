import json

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from mock import patch

from typeform_feedback.models import (
    UserGenericTypeformFeedback,
)

from .test_mixin import TypeformTestMixin


class TestTypeformSignals(TypeformTestMixin, TestCase):

    @patch('typeform_feedback.signals_define.new_user_typeform_response.send')
    def test_signal_sended_when_a_new_response_is_received(self, new_response_signal):
        # PREPARE DATA
        url = reverse('webhooks:generic-typeform')

        user, generic_typeform = self.create_base_context()
        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )

        # DO ACTION
        self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        user_response = UserGenericTypeformFeedback.objects.get(
            feedback=generic_typeform,
            user=user,
        )
        self.assertTrue(new_response_signal.called)
        self.assertEqual(user_response.status, settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_ANSWERED)
        self.assertEqual(len(user_response.responses), 1)

    @patch('typeform_feedback.signals_define.new_user_typeform_response.send')
    def test_signal_sended_when_a_new_response_send_only_one_time(self, new_response_signal):
        # PREPARE DATA
        url = reverse('webhooks:generic-typeform')

        user, generic_typeform = self.create_base_context()
        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        user_response.set_typeform_response(
            self.typeform_with_hidden_fields_response_payload(
                user_pk=user.pk,
                typeform_id=generic_typeform.typeform_id,
            )
        )
        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )

        self.client.post(
            reverse('api:action-validate', kwargs={'uuid': user_response.uuid}),
            data=json.dumps({}),
            content_type='application/json',
        )

        # DO ACTION
        self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertTrue(new_response_signal.called)
        self.assertEqual(user_response.status, settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_DONE)
        self.assertFalse(settings.TYPEFORM_FEEDBACK_NOTIFICATE_ALL_USER_RESPONSES)
        self.assertEqual(len(user_response.responses), 2)
        self.assertEqual(new_response_signal.call_count, 1)

    @patch('typeform_feedback.signals_define.user_response_approved.send')
    def test_signal_sended_when_an_user_response_is_approved(self, response_approved_signal):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )
        user_response.set_typeform_response(user_response_payload)

        # DO ACTION
        self.client.post(
            reverse('api:action-validate', kwargs={'uuid': user_response.uuid}),
            data=json.dumps({}),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertTrue(response_approved_signal.called)
