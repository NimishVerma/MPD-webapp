from django.db import models
import os
from django.conf import settings
# Create your models here.
def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join('photos', str(instance.id), filename)


class DownloadedVideos(models.Model):
	path = models.FilePathField(path=settings.MEDIA_ROOT)

	name = models.TextField(null=True, blank = True)
	

	def __str__(self):
		if self.name:
			return self.name
		else:
			return "rekt"