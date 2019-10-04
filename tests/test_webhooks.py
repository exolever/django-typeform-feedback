import json

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from foo.models import Foo
from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback, UserGenericTypeformFeedback


from .test_mixin import TypeformTestMixin


class TestTypeformWebhooks(TypeformTestMixin, TestCase):

    def test_payload_for_generic_typeform_is_stored(self):
        # PREPARE DATA

        user = get_user_model()(
            username='testuser',
            email='user@example.com',
        )
        user.save()

        foo = Foo(bar='bar')
        foo.save()

        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
            typeform_id=generic_typeform.typeform_id,
        )

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=user.pk,
                feedback__content_type=ContentType.objects.get_for_model(foo),
                feedback__object_id=foo.pk,
            ).exists()
        )

    def test_payload_for_unknown_form_is_ignored(self):
        # PREPARE DATA
        user = get_user_model()(
            username='testuser',
            email='user@example.com',
        )
        user.save()

        foo = Foo(bar='bar')
        foo.save()

        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=user.pk,
        )

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=user.pk,
                feedback__content_type=ContentType.objects.get_for_model(foo),
                feedback__object_id=foo.pk,
            ).exists()
        )

    def test_payload_for_unknown_user_is_ignored(self):
        # PREPARE DATA
        unexistsing_user_pk = '9999999999'
        foo = Foo(bar='bar')
        foo.save()

        url = reverse('webhooks:generic-typeform')

        # DO ACTION
        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

        user_response_payload = self.typeform_with_hidden_fields_response_payload(
            user_pk=unexistsing_user_pk,
            typeform_id=generic_typeform.typeform_id,
        )

        # DO ACTION
        response = self.client.post(
            url,
            data=json.dumps(user_response_payload),
            content_type='application/json',
        )

        # ASSERTIONS
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            UserGenericTypeformFeedback.objects.filter(
                user__pk=unexistsing_user_pk,
                feedback__content_type=ContentType.objects.get_for_model(foo),
                feedback__object_id=foo.pk,
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
        self.assertEqual(response.status_code, 200)
