from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	def user_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
		return 'res/user_{0}/%Y/%m/%d/{1}'.format(instance.user.id, filename)

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	attached_photo = models.ImageField(upload_to=user_directory_path)
	attached_file = models.FileField(upload_to=user_directory_path)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
