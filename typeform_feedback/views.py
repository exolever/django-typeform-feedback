# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	GenericTypeformFeedback,
	UserGenericTypeformFeedback,
)


class GenericTypeformFeedbackCreateView(CreateView):

    model = GenericTypeformFeedback


class GenericTypeformFeedbackDeleteView(DeleteView):

    model = GenericTypeformFeedback


class GenericTypeformFeedbackDetailView(DetailView):

    model = GenericTypeformFeedback


class GenericTypeformFeedbackUpdateView(UpdateView):

    model = GenericTypeformFeedback


class GenericTypeformFeedbackListView(ListView):

    model = GenericTypeformFeedback


class UserGenericTypeformFeedbackCreateView(CreateView):

    model = UserGenericTypeformFeedback


class UserGenericTypeformFeedbackDeleteView(DeleteView):

    model = UserGenericTypeformFeedback


class UserGenericTypeformFeedbackDetailView(DetailView):

    model = UserGenericTypeformFeedback


class UserGenericTypeformFeedbackUpdateView(UpdateView):

    model = UserGenericTypeformFeedback


class UserGenericTypeformFeedbackListView(ListView):

    model = UserGenericTypeformFeedback

