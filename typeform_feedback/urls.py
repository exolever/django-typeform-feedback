# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'typeform_feedback'
urlpatterns = [
    url(
        regex="^GenericTypeformFeedback/~create/$",
        view=views.GenericTypeformFeedbackCreateView.as_view(),
        name='GenericTypeformFeedback_create',
    ),
    url(
        regex="^GenericTypeformFeedback/(?P<pk>\d+)/~delete/$",
        view=views.GenericTypeformFeedbackDeleteView.as_view(),
        name='GenericTypeformFeedback_delete',
    ),
    url(
        regex="^GenericTypeformFeedback/(?P<pk>\d+)/$",
        view=views.GenericTypeformFeedbackDetailView.as_view(),
        name='GenericTypeformFeedback_detail',
    ),
    url(
        regex="^GenericTypeformFeedback/(?P<pk>\d+)/~update/$",
        view=views.GenericTypeformFeedbackUpdateView.as_view(),
        name='GenericTypeformFeedback_update',
    ),
    url(
        regex="^GenericTypeformFeedback/$",
        view=views.GenericTypeformFeedbackListView.as_view(),
        name='GenericTypeformFeedback_list',
    ),
	url(
        regex="^UserGenericTypeformFeedback/~create/$",
        view=views.UserGenericTypeformFeedbackCreateView.as_view(),
        name='UserGenericTypeformFeedback_create',
    ),
    url(
        regex="^UserGenericTypeformFeedback/(?P<pk>\d+)/~delete/$",
        view=views.UserGenericTypeformFeedbackDeleteView.as_view(),
        name='UserGenericTypeformFeedback_delete',
    ),
    url(
        regex="^UserGenericTypeformFeedback/(?P<pk>\d+)/$",
        view=views.UserGenericTypeformFeedbackDetailView.as_view(),
        name='UserGenericTypeformFeedback_detail',
    ),
    url(
        regex="^UserGenericTypeformFeedback/(?P<pk>\d+)/~update/$",
        view=views.UserGenericTypeformFeedbackUpdateView.as_view(),
        name='UserGenericTypeformFeedback_update',
    ),
    url(
        regex="^UserGenericTypeformFeedback/$",
        view=views.UserGenericTypeformFeedbackListView.as_view(),
        name='UserGenericTypeformFeedback_list',
    ),
	]
