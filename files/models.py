from django.db import models
import os
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
from .constants import *
import logging

logger = logging.getLogger(__name__)


class Base(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="%(class)s_objects", null=True, blank=True)
	title = models.CharField(max_length=255, blank=True)
	uuid_id = models.UUIDField(editable=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class Directory(Base):
	directories = models.ForeignKey('self', on_delete=models.CASCADE, related_name="directories_of_this", null=True, blank=True)

	def save(self, *args, **kwargs):
		self.uuid_id = uuid.uuid4()

		super(Directory, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Directory"
		verbose_name_plural = "Directories"
		ordering = ("-created", )

	def __str__(self):
		return f"{self.title}"	

	def get_absolute_url(self):
		return reverse('files:files-list-detail', args=[self.uuid_id])	


class File(Base):
	file = models.FileField(upload_to="users/files/%Y/%m/%d")
	directory = models.ForeignKey('Directory', on_delete=models.CASCADE, related_name="files_set", null=True, blank=True)
	file_type = models.CharField(max_length=100, null=True, blank=True)

	# geting file extension
	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return (name, extension)

	def process_title(self, title):
		title = self.extension()[0].split('/')
		length = len(title)
		title = title[length - 1]	
		logger.warning("Processing title")
		return title

	def match_type(self, ext):
		logger.warning("Matching file type")

		if ext in WORD:
			self.file_type = "#Word"
		elif ext in EXCEL:
			self.file_type = "#Excel"
		elif ext in POWER_POINT:
			self.file_type = "#PowerP"
		elif ext in IMAGE_TYPES:
			self.file_type = "#Image"
		elif ext in PDF:
			self.file_type = "#PDF"		
		elif ext in VIDEO:
			self.file_type = "#Video"
		else:
			self.file_type = "#UnknownFile"			
		
	# file type specification 
	def save(self, *args, **kwargs):
		title = self.extension()[0].split('/')
		extension_type = self.extension()[1]
		self.title = self.process_title(title)
		self.uuid_id = uuid.uuid4()		
		self.match_type(extension_type)
		
		super(File, self).save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse("files:file-detail", args=[self.uuid_id])

	def __str__(self):
		return f"{self.title}{self.extension()[1]}"


class Department(models.Model):
	name = models.CharField(max_length=255)


user_model = get_user_model()
user_model.add_to_class('department', models.ForeignKey(Department, related_name='employees', on_delete=models.SET_NULL, null=True, blank=True))
