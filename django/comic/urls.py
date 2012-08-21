from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib import admin
from comicsite.models import ComicSite
 
admin.autodiscover()


urlpatterns = patterns('',
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # main page 
    url(r'^$',ListView.as_view(model=ComicSite, template_name='index.html'),name = 'home'),
    #url(r'^Comic/$',ListView.as_view(model=ComicSite, template_name='index.html'),name = 'home'),
     
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^site/',include('comicsite.urls')),
        
    
    # requirement for social_auth
    url(r'',include('social_auth.urls')),
    # all normal accounts stuff is redirected to accounts
    url(r'^accounts/',include('profiles.urls')),
    
    #temporary url to test MeVisLab visualisation. This should be moved to a seperate MeVis app
    url(r'^mevislab_visualisation', 'mevislab_visualisation.views.index'),
    
)
    
