from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback, UserGenericTypeformFeedback

from foo.models import Foo

from .test_mixin import TypeformTestMixin


class TestTypeformRedirectView(TypeformTestMixin, TestCase):

    def test_redirect_view(self):
        # PREPARE DATA
        _, generic_typeform = self.create_base_context()
        url = reverse('typeform:get-quiz', kwargs={'quiz_slug': generic_typeform.quiz_slug})

        # DO ACTION
        response = self.client.get(url)

        # ASSERTIONS
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            settings.TYPEFORM_FEEDBACK_DEFAULT_URL.format(generic_typeform.typeform_id)
        )

    def test_redirect_view_for_logged_user(self):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user.set_password('abc')
        user.save()

        url = reverse('typeform:get-quiz', kwargs={'quiz_slug': generic_typeform.quiz_slug})
        assert self.client.login(username=user.username, password='abc')

        # DO ACTION
        response = self.client.get(url)

        # ASSERTIONS
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            settings.TYPEFORM_FEEDBACK_DEFAULT_URL.format(generic_typeform.typeform_id)
            in
            response.url
        )
        self.assertTrue('user_id={}'.format(user.pk) in response.url)
        print(response.url)

    def test_mark_user_response_as_approved(self):
        user, generic_typeform = self.create_base_context()
        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        url = reverse('typeform:validate', kwargs={'uuid': user_response.uuid})

        # DO ACTION
        response = self.client.get(url)

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_response.status, settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_DONE)

    def test_mark_user_response_as_fail(self):
        user, generic_typeform = self.create_base_context()

        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        url = reverse('typeform:invalidate', kwargs={'uuid': user_response.uuid})

        # DO ACTION
        response = self.client.get(url)

        # ASSERTIONS
        user_response.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_response.status, settings.TYPEFORM_FEEDBACK_USER_FEEDBACK_STATUS_FAIL)
