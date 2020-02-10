from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
