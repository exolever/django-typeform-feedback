=====
Usage
=====

To use django-typeform-feedback in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'typeform_feedback.apps.TypeformFeedbackConfig',
        ...
    )

Add django-typeform-feedback's URL patterns:

.. code-block:: python

    from typeform_feedback import urls as typeform_feedback_urls


    urlpatterns = [
        ...
        url(r'^', include(typeform_feedback_urls)),
        ...
    ]
