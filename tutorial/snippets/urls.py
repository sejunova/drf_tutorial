from django.conf.urls import url, include

from .views import snippet_list

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list')
]