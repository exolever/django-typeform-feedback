import json

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from typeform_feedback.models import UserGenericTypeformFeedback

from .test_mixin import TypeformTestMixin


class TestTypeformWebhooks(TypeformTestMixin, TestCase):

    def test_payload_for_generic_typeform_is_stored(self):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )
        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            UserGenericTypeformFeedback.objects.get(
                user__pk=user.pk,
                feedback__content_type=ContentType.objects.get_for_model(generic_typeform.related_to),
                feedback__object_id=generic_typeform.related_to.pk,
            ).status,
            settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_ANSWERED,
        )
        self.assertTrue(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=user.pk,
                feedback__content_type=ContentType.objects.get_for_model(generic_typeform.related_to),
                feedback__object_id=generic_typeform.related_to.pk,
            ).exists()
        )

    def test_payload_for_unknown_form_is_ignored(self):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
        )
        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=user.pk,
                feedback__content_type=ContentType.objects.get_for_model(generic_typeform.related_to),
                feedback__object_id=generic_typeform.related_to.pk,
            ).exists()
        )

    def test_payload_for_unknown_user_is_ignored(self):
        # PREPARE DATA
        unexistsing_user_pk = '9999999999'
        _, generic_typeform = self.create_base_context()
        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=unexistsing_user_pk,
            typeform_id=generic_typeform.typeform_id,
        )
        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=unexistsing_user_pk,
                feedback__content_type=ContentType.objects.get_for_model(generic_typeform.related_to),
                feedback__object_id=generic_typeform.related_to.pk,
            ).exists()
        )

    def test_payload_for_non_generic_typeform_is_ignored(self):
        # PREPARE DATA
        user_response_payload = self.typeform_without_hidden_fields_response_payload()
        url = reverse('webhooks:generic-typeform')

        # DO ACTIONS
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
