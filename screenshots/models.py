from django_extensions.db.fields import CreationDateTimeField
from django.db import models
from fabric.api import local
from django.conf import settings
import os

class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshots', null = True, blank = True)
    url = models.URLField(verify_exists=False)
    created = CreationDateTimeField()

    def save_screenshot(self, delay = 3):
        screenshot = os.path.join("screenshots", "%i.png" % self.id)
        screenshot_path = os.path.join(settings.MEDIA_ROOT, screenshot)
        a = local('xvfb-run -s "-screen 0 1024x768x24" %s -d %i -t 200x200 %s -f %s' %  (
                                                                                        settings.PYWEBSHOT_PATH,
                                                                                        delay,
                                                                                        self.url,
                                                                                        screenshot_path
                                                                                        ))
        self.image = screenshot
        self.save()

        
