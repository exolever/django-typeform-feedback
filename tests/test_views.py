from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback, UserGenericTypeformFeedback

from foo.models import Foo


class TestTypeformRedirectView(TestCase):

    def test_redirect_view(self):
        # PREPARE DATA
        foo = Foo(bar='bar')
        foo.save()

        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )
        url = reverse('typeform:get-quiz', kwargs={'quiz_slug': generic_typeform.quiz_slug})

        # DO ACTION
        response = self.client.get(url)

        # ASSERTIONS
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            settings.TYPEFORM_FEEDBACK_DEFAULT_URL.format(generic_typeform.typeform_id)
        )

    def test_mark_user_response_as_approved(self):
        foo = Foo(bar='bar')
        foo.save()
        user = get_user_model()(
            username='Test User',
            email='user@example.com',
        )
        user.save()

        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

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
        foo = Foo(bar='bar')
        foo.save()
        user = get_user_model()(
            username='Test User',
            email='user@example.com',
        )
        user.save()

        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

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
