from django_extensions.db.fields import CreationDateTimeField, UUIDField
from django.db import models
from fabric.api import local
from django.conf import settings
import os

class Screenshot(models.Model):
    uuid = UUIDField()
    image = models.ImageField(upload_to='screenshots', null = True, blank = True)
    url = models.URLField(verify_exists=False)
    created = CreationDateTimeField()

    def save_screenshot(self, size='200x200', delay = 3):
        screenshot = os.path.join("screenshots", "%s.png" % self.uuid)
        screenshot_path = os.path.join(settings.MEDIA_ROOT, screenshot)
        a = local('xvfb-run -s "-screen 0 1024x768x24" %s -d %i -t %s %s -f %s' %  (
                                                                                    settings.PYWEBSHOT_PATH,
                                                                                    delay, size, self.url,
                                                                                    screenshot_path
                                                                                    ))
        self.image = screenshot
        self.save()

        
