from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view='',
        name='question_list'
    ),
    url(
        regex=r'^question/(?P<pk>\d+)/$',
        view=views.test,
        name='question_detail'
    ),
    url(
        regex=r'^popular/$',
        view='',
        name='question_popular'
    ),
    url(
        regex=r'^ask/$',
        view='',
        name='question_ask'
    ),
    url(
        regex=r'^answer/$',
        view='',
        name='question_answer'
    ),
    url(
        regex=r'^signup/$',
        view='',
        name='signup'
    ),
    url(
        regex=r'^login/$',
        view='',
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view='',
        name='logout'
    ),
    url(
        regex=r'^new/$',
        view='',
        name='question_new'
    ),
]