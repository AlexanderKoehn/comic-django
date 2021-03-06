from django.conf.urls import *

urlpatterns = patterns('filetransfers.views',
    (r'^$', 'upload_handler'),
    (r'^download/(?P<pk>\d+)$', 'download_handler'),
    (r'^serve/(?P<pk>\d+)$', 'uploadedfileserve_handler'),
    #url(r'^(?P<site_short_name>\w+)/(?P<page_title>\w+)/$','comicsite.views.page'),
    (r'^download/(?P<project_name>[\w-]+)/(?P<dataset_title>[\w-]+)/(?P<filename>.+)/$', 'download_handler_dataset_file'),
    (r'^delete/(?P<pk>.+)$', 'delete_handler'),
)
