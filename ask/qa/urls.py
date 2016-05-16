from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.test,
        name='question_list'
    ),
    url(
        regex=r'^question/(?P<pk>\d+)/$',
        view=views.test,
        name='question_detail'
    ),
    url(
        regex=r'^popular/$',
        view=views.test,
        name='question_popular'
    ),
    url(
        regex=r'^ask/$',
        view=views.test,
        name='question_ask'
    ),
    url(
        regex=r'^answer/$',
        view=views.test,
        name='question_answer'
    ),
    url(
        regex=r'^signup/$',
        view=views.test,
        name='signup'
    ),
    url(
        regex=r'^login/$',
        view=views.test,
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=views.test,
        name='logout'
    ),
    url(
        regex=r'^new/$',
        view=views.test,
        name='question_new'
    ),
]