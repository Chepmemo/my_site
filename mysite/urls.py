from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from polls import api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/polls/questions$', api.QuestionList.as_view()),
    url(r'^api/polls/questions/(?P<pk>[0-9]+)$', api.QuestionDetail.as_view()),
    url(r'^api/polls/choice$', api.ChoiceList.as_view()),
    url(r'^api/polls/choice/(?P<pk>[0-9]+)$', api.ChoiceDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
