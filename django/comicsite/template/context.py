"""
 Custom processors to pass variables to views rendering template tags 
 see http://www.djangobook.com/en/2.0/chapter09.html  
"""

from django.template import RequestContext
from django.core.exceptions import ImproperlyConfigured

class ComicSiteRequestContext(RequestContext):
    """ RequestContext with added comicsite. Could not get comicsite from httprequest so
        passing it in init()"""
    # I want to add comicsite instance to current context so that template tags know
    # which comicsite is rendering them. You can add a custom context processor to 
    # requestContext but this can only return variables based on the given httpcontext
    # This does not contain any info on which comicsite is rendering, so I chose to add
    # comicsite param to init.
    
    # FIXME: I think this class should be refactored into something which is listed
    # in TEMPLATE_CONTEXT_PROCESSORS and adds the current page to the context.
    # see https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext
        
    def __init__(self,request,page=None,*args,**kwargs):
        super(ComicSiteRequestContext, self).__init__(request,*args,**kwargs)
        self.page = page        
        self.fullpath = request.get_full_path() # Not sure about adding vars here
                                                # there has to be an easier django
                                                # based solution..
        
        #TODO: Using request here to transport some variables into context. This
        # seems quite weird. But how to do it better?
        if hasattr(request,"pages"):
            self.pages = request.pages
        if hasattr(request,"site"):
            self.site = request.site
                            
        #add context url parameters (?var1=value) to context to be able to render 
        #them in template
        self.update(request.GET)
        
        
 

class CurrentAppRequestContext(RequestContext):
    """ sets current_app in request so any reversing of admin urls goes right.
    Project admin needs currentapp = '<projectname>admin' to refer to admin 
    of that project. Without this request context, urls would reverse to main/root
    admin instead of projectadmin """
    
        
    def __init__(self,request,page=None,*args,**kwargs):
        super(CurrentAppRequestContext, self).__init__(request,*args,**kwargs)
        
        if not hasattr(request,"projectname"):
            raise ImproperlyConfigured("CurrentAppRequestContext requires " 
            "project middleware to know which project the request is coming from")
        from comicmodels.models import get_project_admin_instance_name
        self.current_app = get_project_admin_instance_name(request.projectname) 
 
