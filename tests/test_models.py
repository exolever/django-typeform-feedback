from django.test import TestCase

from foo.models import Foo

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback, UserGenericTypeformFeedback

from .test_mixin import TypeformTestMixin


class TestTypeformModels(TypeformTestMixin, TestCase):

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

    def test_parse_questions_from_response(self):
        # PREPARE DATA
        user, generic_typeform = self.create_base_context()
        user_response_payload = self.all_type_questions_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )
        user_response = UserGenericTypeformFeedback(
            feedback=generic_typeform,
            user=user,
        )
        user_response.save()

        # DO ACTION
        parsed_response = user_response.parse_response(user_response_payload)

        # ASSERTIONS
        self.assertEqual(len(parsed_response), 14)  # Total question parsed
        self.assertEqual(
            len(list(filter(lambda x: x.get('id') == 'Ma4sfFA5CgkN', parsed_response))[0].get('options')),
            3,
        )
        self.assertEqual(
            len(list(filter(lambda x: x.get('id') == 'ffgm9HcOu3kK', parsed_response))[0].get('options')),
            4,
        )
        self.assertEqual(                           # Short text questions
            len(list(filter(lambda x: x.get('type') == 'short_text', parsed_response))),
            1
        )
        self.assertEqual(                           # Long text questions
            len(list(filter(lambda x: x.get('type') == 'long_text', parsed_response))),
            1
        )
        self.assertEqual(                           # Choice questions
            len(list(filter(lambda x: x.get('type') == 'multiple_choice', parsed_response))),
            2
        )
        self.assertEqual(                           # Boolean questions
            len(list(filter(lambda x: x.get('type') == 'yes_no', parsed_response))),
            1
        )
        self.assertEqual(                           # Email questions
            len(list(filter(lambda x: x.get('type') == 'email', parsed_response))),
            1
        )
        self.assertEqual(                           # Scale questions
            len(list(filter(lambda x: x.get('type') == 'opinion_scale', parsed_response))),
            1
        )
        self.assertEqual(                           # Rating questions
            len(list(filter(lambda x: x.get('type') == 'rating', parsed_response))),
            1
        )
        self.assertEqual(                           # Date questions
            len(list(filter(lambda x: x.get('type') == 'date', parsed_response))),
            1
        )
        self.assertEqual(                           # Number questions
            len(list(filter(lambda x: x.get('type') == 'number', parsed_response))),
            1
        )
        self.assertEqual(                           # Legal questions
            len(list(filter(lambda x: x.get('type') == 'legal', parsed_response))),
            1
        )
        self.assertEqual(                           # File_upload questions
            len(list(filter(lambda x: x.get('type') == 'file_upload', parsed_response))),
            1
        )
        self.assertEqual(                           # Website questions
            len(list(filter(lambda x: x.get('type') == 'website', parsed_response))),
            1
        )
        self.assertEqual(                           # dropdown questions
            len(list(filter(lambda x: x.get('type') == 'dropdown', parsed_response))),
            1
        )
