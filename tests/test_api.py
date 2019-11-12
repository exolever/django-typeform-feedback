from django.conf import settings
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from foo.models import Foo
from typeform_feedback.models import UserGenericTypeformFeedback, GenericTypeformFeedback
from typeform_feedback.helpers import random_string

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

    def test_get_typeform_url(self):
        user, generic_typeform = self.create_base_context()
        user.set_password('abc')
        user.save()
        self.client.login(username=user.username, password='abc')

        # DO ACTION
        response = self.client.get(
            reverse('api:get-url', kwargs={'quiz_slug': generic_typeform.quiz_slug})
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'url': '{}?user_id={}'.format(
                settings.TYPEFORM_FEEDBACK_DEFAULT_URL.format(generic_typeform.typeform_id),
                user.pk)
            }
        )

    def test_get_typeform_url_for_not_real_typeform(self):
        user, _ = self.create_base_context()
        user.set_password('abc')
        user.save()

        foo = Foo(bar='bar')
        foo.save()
        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id='',
            url='https://fakeurl.com',
        )
        self.client.login(username=user.username, password='abc')

        # DO ACTION
        response = self.client.get(
            reverse('api:get-url', kwargs={'quiz_slug': generic_typeform.quiz_slug})
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'url': '{}?user_id={}'.format(
                generic_typeform.url,
                user.pk)
            }
        )
