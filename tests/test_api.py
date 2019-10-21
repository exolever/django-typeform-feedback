from django.conf import settings
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from typeform_feedback.models import UserGenericTypeformFeedback

from .test_mixin import TypeformTestMixin


class TestAPI(TypeformTestMixin, APITestCase):

    def test_action_validate_pending_user_response(self):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        # DO ACTION
        response = self.client.post(
            reverse('api:action-validate', kwargs={'uuid': user_response.uuid}),
            data={},
            content_type='application/json',
        )

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            user_response.status,
            settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_PENDING,
        )

    def test_action_validate_user_response(self):
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
        response = self.client.post(
            reverse('api:action-validate', kwargs={'uuid': user_response.uuid}),
            data={},
            content_type='application/json',
        )

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            user_response.status,
            settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_DONE,
        )

    def test_action_validate_previous_failed_response_for_user(self):
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
        user_response.mark_as_fail()

        # DO ACTION
        response = self.client.post(
            reverse('api:action-validate', kwargs={'uuid': user_response.uuid}),
            data={},
            content_type='application/json',
        )

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            user_response.status,
            settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_DONE,
        )

    def test_action_invalidate_user_response(self):
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
        response = self.client.post(
            reverse('api:action-invalidate', kwargs={'uuid': user_response.uuid}),
            data={},
            content_type='application/json',
        )

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            user_response.status,
            settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_FAIL,
        )
