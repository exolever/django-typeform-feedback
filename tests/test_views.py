from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback

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
