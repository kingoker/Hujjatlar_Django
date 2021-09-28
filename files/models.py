from django.db import models
import os
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class Directory(models.Model):
	title = models.CharField(max_length=255)
	directories = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="directories_of_this", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Directory, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Directory"
		verbose_name_plural = "Directories"
		ordering = ("-created", )

	def __str__(self):
		return f"{self.title}"	

	def get_absolute_url(self):
		return reverse('files:files-list-detail', args=[self.slug])	

class File(models.Model):
	title = models.CharField(max_length=255)
	file = models.FileField(upload_to="users/files/%Y/%m/%d")
	directory = models.ForeignKey('Directory', on_delete=models.SET_NULL, related_name="files_set", null=True, blank=True)
	slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		# print(name, extension)
		return (name, extension)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(File, self).save(*args, **kwargs)

	
	def get_absolute_url(self):
		return reverse("files:file-detail", args=[self.slug])
	def __str__(self):
		return f"{self.title}{self.extension()[1]}"

