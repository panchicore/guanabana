from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from api.handlers import ScreenshotterHandler

auth = HttpBasicAuthentication(realm='My sample API')

screenshot = Resource(handler=ScreenshotterHandler)

urlpatterns = patterns('',
    url(r'^screenshot/$', screenshot, name='screenshot'),
    # automated documentation
    url(r'^$', documentation_view),
)
