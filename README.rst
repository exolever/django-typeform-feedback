=============================
django-typeform-feedback
=============================

.. image:: https://badge.fury.io/py/django-typeform-feedback.svg
    :target: https://badge.fury.io/py/django-typeform-feedback

.. image:: https://requires.io/github/exolever/django-typeform-feedback/requirements.svg?branch=master
     :target: https://requires.io/github/exolever/django-typeform-feedback/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://travis-ci.org/exolever/django-typeform-feedback.svg?branch=master
    :target: https://travis-ci.org/exolever/django-typeform-feedback

.. image:: https://codecov.io/gh/exolever/django-typeform-feedback/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/exolever/django-typeform-feedback

Your project description goes here

Quickstart
----------

Install django-typeform-feedback::

    pip install exolever/django-typeform-feedback

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'typeform_feedback',
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

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
