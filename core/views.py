from django.views import View
from django.http import HttpResponse

__all__ = ['IndexView']


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Index page')
