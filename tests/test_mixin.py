import random
import string

from typeform_feedback.helpers import random_string


class TypeformTestMixin:

    def typeform_with_hidden_fields_response_payload(self, user_pk, typeform_id=None):
        typeform_code = typeform_id or  random_string(5)

        return {
            'event_id': '01DNPVTH0DHXGKX5PFA073K3AM',
            'event_type': 'form_response',
            'form_response': {
                'form_id': typeform_code,
                'token': '01DNPVTH0DHXGKX5PFA073K3AM',
                'landed_at': '2019-09-26T13:23:03Z',
                'submitted_at': '2019-09-26T13:23:03Z',
                'hidden': {
                    'user_id': user_pk
                },
                'definition': {
                    'id': typeform_code,
                    'title': 'Form with user id',
                    'fields': [
                        {
                            'id': 'KSExiY3iNRBS',
                            'title': 'Test',
                            'type': 'short_text',
                            'ref': '57373ea0-4a4f-42a3-aa4c-2d6a242a63eb',
                            'properties': {}
                        }
                    ],
                    'hidden': [
                        'user_id'
                    ]
                },
                'answers': [
                    {
                        'type': 'text',
                        'text': 'Lorem ipsum dolor',
                        'field': {
                            'id': 'KSExiY3iNRBS',
                            'type': 'short_text',
                            'ref': '57373ea0-4a4f-42a3-aa4c-2d6a242a63eb'
                        }
                    }
                ]
            }
        }


    def typeform_without_hidden_fields_response_payload(self, typeform_id=None):
        typeform_code = typeform_id or  random_string(5)

        return {
            'event_id': '01DNPTRY6HV49ZZXY4B11CWZ3Y',
            'event_type': 'form_response',
            'form_response': {
                'form_id': typeform_code,
                'token': '01DNPTRY6HV49ZZXY4B11CWZ3Y',
                'landed_at': '2019-09-26T13:04:43Z',
                'submitted_at': '2019-09-26T13:04:43Z',
                'definition': {
                    'id': typeform_code,
                    'title': 'No user id',
                    'fields': [
                        {
                            'id': 'UchwRzy4mXjO',
                            'title': 'Hello',
                            'type': 'short_text',
                            'ref': 'bfe9080f-7926-4194-befa-db472c53dddc',
                            'properties': {}
                        }
                    ]
                },
                'answers': [
                    {
                        'type': 'text',
                        'text': 'Lorem ipsum dolor',
                        'field': {
                            'id': 'UchwRzy4mXjO',
                            'type': 'short_text',
                            'ref': 'bfe9080f-7926-4194-befa-db472c53dddc'
                        }
                    }
                ]
            }
        }
