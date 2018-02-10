from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadlist/$', views.upload_file, name='uploadfile'),
    url(r'^form/$', views.dictation_form, name='dicatationform'),
    url(r'^words/$' , views.word_voice, name='wordvoice')
]