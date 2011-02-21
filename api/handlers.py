from piston.handler import BaseHandler
from piston.utils import rc

ALL = ('GET', 'POST', 'PUT', 'DELETE')
 

class ScreenshotterHandler(BaseHandler):
    allowed_methods = ALL

    def read(self, request):
        return {"method":"GET"}

    def create(self, request):
        return rc.CREATED


