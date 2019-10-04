from django.test import TestCase

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback

from foo.models import Foo


class TestTypeformRedirectView(TestCase):

    def test_create_generic_typeform(self):
        # PREPARE DATA
        foo = Foo(bar='bar')
        foo.save()

        # DO ACTION
        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

        # ASSERTIONS
        self.assertEqual(generic_typeform.related_to, foo)
        self.assertIsNotNone(generic_typeform.quiz_slug)
        self.assertIsNotNone(generic_typeform.url)
        self.assertIsNotNone(generic_typeform.typeform_id)
