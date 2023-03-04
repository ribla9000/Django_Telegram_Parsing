from django.db import models


class News(models.Model):
	tag = models.CharField(max_length=20, default='')
	title = models.CharField(max_length=64, default='')
	description = models.TextField(default='')
	detail = models.TextField(default='')
	date = models.TextField(default="")
	content = models.TextField(default='')

	class Meta:
		verbose_name = "News"
		verbose_name_plural = "News"
