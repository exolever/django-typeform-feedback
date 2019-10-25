from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView

from ..models import GenericTypeformFeedback


class GetQuizView(DetailView):

    model = GenericTypeformFeedback
    slug_field = 'quiz_slug'
    slug_url_kwarg = 'quiz_slug'

    def get(self, request, *args, **kwargs):
        url_param = ''
        if not request.user.is_anonymous:
            url_param = '?user_id={}'.format(request.user.pk)

        return HttpResponseRedirect(
            '{}{}'.format(
                self.get_object().url,
                url_param,
            )
        )
