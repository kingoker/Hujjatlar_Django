from django.db import models
import os
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


WORD = (
	".docx",".doc", ".docm", ".dotx", ".dotm", ".odt"
	)

EXCEL = (
	".xlsx", ".xlsm", ".xltx", ".xltm", ".xlsb", ".xlam",
	)

POWER_POINT = (
	".pptx", ".pptm", ".potx", ".potm", ".ppam", 
	".ppsx", ".ppsm", ".sldx", ".sldm", ".thmx",
	)

IMAGE_TYPES = (".jpeg", ".png", ".jpg", )

PDF = (".pdf")

VIDEO = (".mp4", ".mov", ".mkv", ".m4v", ".avi", ".flv", ".3gp", ".")

class Base(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="%(class)s_objects", null=True, blank=True)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class Directory(Base):
	directories = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="directories_of_this", null=True, blank=True)

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


class File(Base):
	file = models.FileField(upload_to="users/files/%Y/%m/%d")
	directory = models.ForeignKey('Directory', on_delete=models.SET_NULL, related_name="files_set", null=True, blank=True)
	file_type = models.CharField(max_length=100, null=True, blank=True)
	
	# geting file extension
	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return (name, extension)

	# file type specification 
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)

		if self.extension()[1] in WORD:
			self.file_type = "#Word"
		elif self.extension()[1] in EXCEL:
			self.file_type = "#Excel"
		elif self.extension()[1] in POWER_POINT:
			self.file_type = "#PowerP"
		elif self.extension()[1] in IMAGE_TYPES:
			self.file_type = "#Image"
		elif self.extension()[1] in PDF:
			self.file_type = "#PDF"		
		elif self.extension()[1] in VIDEO:
			self.file_type = "#Video"

		else:
			self.file_type = "#UnknownFile"			
		
		super(File, self).save(*args, **kwargs)

	
	def get_absolute_url(self):
		return reverse("files:file-detail", args=[self.slug])
	

	def __str__(self):
		return f"{self.title}{self.extension()[1]}"



class Department(models.Model):
	name = models.CharField(max_length=255)


user_model = get_user_model()
user_model.add_to_class('department',
                        models.ForeignKey(Department, related_name='employees', on_delete=models.SET_NULL, null=True, blank=True))	