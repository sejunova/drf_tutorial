from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import snippet_list, snippet_detail

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)