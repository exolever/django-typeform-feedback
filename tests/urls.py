from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/', include('typeform_feedback.api.urls', namespace='api')),
    url(r'^typeform/', include('typeform_feedback.urls', namespace='typeform')),
    url(r'^webhooks/', include('typeform_feedback.urls_webhooks', namespace='webhooks')),
]
