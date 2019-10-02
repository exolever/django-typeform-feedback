from django.conf.urls import url

from .views import GetQuizView

app_name = 'typeform_feedback'

urlpatterns = [
    url(r'^generic/(?P<quiz_slug>[a-z A-Z _]+)/$', GetQuizView.as_view(), name='get-quiz'),
]
