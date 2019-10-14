from django.contrib.auth import get_user_model

from typeform_feedback.helpers import random_string
from typeform_feedback.models import GenericTypeformFeedback

from foo.models import Foo

# Definition because of Typeform response
true = True
false = False


class TypeformTestMixin:

    def create_base_context(self):
        foo = Foo(bar='bar')
        foo.save()

        user = get_user_model()(
            username='testuser',
            email='user@example.com',
        )
        user.save()

        generic_typeform = GenericTypeformFeedback.create_typeform(
            linked_object=foo,
            slug=random_string(),
            typeform_id=random_string(5),
        )

        return user, generic_typeform

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

    def all_type_questions_payload(self, user_pk, typeform_id=None):
        typeform_code = typeform_id or  random_string(5)

        return {
            "event_id": "01DQ4RFCJ3FYW3TJH5E845ETDC",
            "event_type": "form_response",
            "form_response": {
                "form_id": typeform_code,
                "token": "6lj2sgwft6yrqolwjo6lj2sg2abfk86z",
                "landed_at": "2019-10-14T09:07:39Z",
                "submitted_at": "2019-10-14T09:09:36Z",
                "hidden": {
                    "user_id": user_pk
                },
                "definition": {
                    "id": typeform_code,
                    "title": "Form with user id",
                    "fields": [
                        {
                            "id": "KSExiY3iNRBS",
                            "title": "Short text type",
                            "type": "short_text",
                            "ref": "57373ea0-4a4f-42a3-aa4c-2d6a242a63eb",
                            "properties": {}
                        },
                        {
                            "id": "Vz8zmkTTCrFk",
                            "title": "Long text type",
                            "type": "long_text",
                            "ref": "39b54dbb-ce22-405c-8789-420c533e27c7",
                            "properties": {}
                        },
                        {
                            "id": "Ma4sfFA5CgkN",
                            "title": "Choice type",
                            "type": "multiple_choice",
                            "ref": "119886c6-e036-4fd5-a471-13ad84429e7f",
                            "properties": {},
                            "choices": [
                                {
                                    "id": "bpwVbdXYPhpc",
                                    "label": "option a"
                                },
                                {
                                    "id": "OHL1XbuWvbG6",
                                    "label": "option b"
                                },
                                {
                                    "id": "RX3PWeDbgIaS",
                                    "label": "option c"
                                }
                            ]
                        },
                        {
                            "id": "ffgm9HcOu3kK",
                            "title": "Multiple choice",
                            "type": "multiple_choice",
                            "allow_multiple_selections": true,
                            "ref": "5bea868e-bc82-486f-b9a0-0ebc1956f302",
                            "properties": {},
                            "choices": [
                                {
                                    "id": "SoL7WOAoqq7n",
                                    "label": "option a"
                                },
                                {
                                    "id": "BAMERMD5ADj0",
                                    "label": "option b"
                                },
                                {
                                    "id": "VzNngc9CLW1B",
                                    "label": "option c"
                                },
                                {
                                    "id": "Dib2T7N6i6hy",
                                    "label": "choice 4"
                                }
                            ]
                        },
                        {
                            "id": "c5jKfLhszNxk",
                            "title": "Boolean type",
                            "type": "yes_no",
                            "ref": "1cac05f6-77c4-4c2e-8880-0b934d34b4cf",
                            "properties": {}
                        },
                        {
                            "id": "BRTvaWh5WBTb",
                            "title": "Email type",
                            "type": "email",
                            "ref": "a5587a39-0cab-4eb0-9c7b-b7f149f8208a",
                            "properties": {}
                        },
                        {
                            "id": "MVhWSkSQIP10",
                            "title": "Scale option",
                            "type": "opinion_scale",
                            "ref": "df83566d-d87a-40cd-aa92-de407bbd8948",
                            "properties": {}
                        },
                        {
                            "id": "TW2QvRWTbbaq",
                            "title": "Rating type",
                            "type": "rating",
                            "ref": "c74aa0fe-24ac-4a90-87e4-5ac8ff86bc80",
                            "properties": {}
                        },
                        {
                            "id": "KBbXJ4eTer6T",
                            "title": "Date type",
                            "type": "date",
                            "ref": "ccd0dec2-b2b5-48e1-8ea6-261ed84d55bd",
                            "properties": {}
                        },
                        {
                            "id": "JoqGdt8hE7N4",
                            "title": "Number type",
                            "type": "number",
                            "ref": "ef22917e-e58c-4e63-a0f9-a6e0c30da422",
                            "properties": {}
                        },
                        {
                            "id": "wCtPd4rKagmR",
                            "title": "Legal type",
                            "type": "legal",
                            "ref": "a21a3a14-901d-4a6b-ada6-bc75a4c4384a",
                            "properties": {}
                        },
                        {
                            "id": "NEHPCi9Wy5PG",
                            "title": "Fileupload type",
                            "type": "file_upload",
                            "ref": "2d5ad39c-c483-404a-b75a-261580f0bed7",
                            "properties": {}
                        },
                        {
                            "id": "BtuqVgfqOhpm",
                            "title": "Website type",
                            "type": "website",
                            "ref": "4e552033-aff4-4785-81fc-6cb8d23d6f12",
                            "properties": {}
                        },
                        {
                            "id": "EssjTUMFNQ8k",
                            "title": "Dropdown type",
                            "type": "dropdown",
                            "ref": "707d7c73-4413-4ff0-ae75-6e014abc838c",
                            "properties": {}
                        }
                    ]
                },
                "answers": [
                    {
                        "type": "text",
                        "text": "short text",
                        "field": {
                            "id": "KSExiY3iNRBS",
                            "type": "short_text",
                            "ref": "57373ea0-4a4f-42a3-aa4c-2d6a242a63eb"
                        }
                    },
                    {
                        "type": "text",
                        "text": "long text",
                        "field": {
                            "id": "Vz8zmkTTCrFk",
                            "type": "long_text",
                            "ref": "39b54dbb-ce22-405c-8789-420c533e27c7"
                        }
                    },
                    {
                        "type": "choice",
                        "choice": {
                            "label": "option a"
                        },
                        "field": {
                            "id": "Ma4sfFA5CgkN",
                            "type": "multiple_choice",
                            "ref": "119886c6-e036-4fd5-a471-13ad84429e7f"
                        }
                    },
                    {
                        "type": "choices",
                        "choices": {
                            "labels": [
                                "option a",
                                "option b"
                            ]
                        },
                        "field": {
                            "id": "ffgm9HcOu3kK",
                            "type": "multiple_choice",
                            "ref": "5bea868e-bc82-486f-b9a0-0ebc1956f302"
                        }
                    },
                    {
                        "type": "boolean",
                        "boolean": true,
                        "field": {
                            "id": "c5jKfLhszNxk",
                            "type": "yes_no",
                            "ref": "1cac05f6-77c4-4c2e-8880-0b934d34b4cf"
                        }
                    },
                    {
                        "type": "email",
                        "email": "mail@domain.com",
                        "field": {
                            "id": "BRTvaWh5WBTb",
                            "type": "email",
                            "ref": "a5587a39-0cab-4eb0-9c7b-b7f149f8208a"
                        }
                    },
                    {
                        "type": "number",
                        "number": 9,
                        "field": {
                            "id": "MVhWSkSQIP10",
                            "type": "opinion_scale",
                            "ref": "df83566d-d87a-40cd-aa92-de407bbd8948"
                        }
                    },
                    {
                        "type": "number",
                        "number": 3,
                        "field": {
                            "id": "TW2QvRWTbbaq",
                            "type": "rating",
                            "ref": "c74aa0fe-24ac-4a90-87e4-5ac8ff86bc80"
                        }
                    },
                    {
                        "type": "date",
                        "date": "2012-05-10",
                        "field": {
                            "id": "KBbXJ4eTer6T",
                            "type": "date",
                            "ref": "ccd0dec2-b2b5-48e1-8ea6-261ed84d55bd"
                        }
                    },
                    {
                        "type": "number",
                        "number": 99,
                        "field": {
                            "id": "JoqGdt8hE7N4",
                            "type": "number",
                            "ref": "ef22917e-e58c-4e63-a0f9-a6e0c30da422"
                        }
                    },
                    {
                        "type": "boolean",
                        "boolean": true,
                        "field": {
                            "id": "wCtPd4rKagmR",
                            "type": "legal",
                            "ref": "a21a3a14-901d-4a6b-ada6-bc75a4c4384a"
                        }
                    },
                    {
                        "type": "file_url",
                        "file_url": "https://api.typeform.com/responses/files/eaa300fe943a27e34c084b9b7c79d88b18d41f4efbb22c35e297dcaa27eebfd7/blank.pdf",
                        "field": {
                            "id": "NEHPCi9Wy5PG",
                            "type": "file_upload",
                            "ref": "2d5ad39c-c483-404a-b75a-261580f0bed7"
                        }
                    },
                    {
                        "type": "url",
                        "url": "https://www.domain.com",
                        "field": {
                            "id": "BtuqVgfqOhpm",
                            "type": "website",
                            "ref": "4e552033-aff4-4785-81fc-6cb8d23d6f12"
                        }
                    },
                    {
                        "type": "choice",
                        "choice": {
                            "label": "option c"
                        },
                        "field": {
                            "id": "EssjTUMFNQ8k",
                            "type": "dropdown",
                            "ref": "707d7c73-4413-4ff0-ae75-6e014abc838c"
                        }
                    }
                ]
            }
        }
