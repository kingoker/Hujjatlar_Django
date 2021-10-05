from django.db import models
import os
from django.template.defaultfilters import slugify
from django.urls import reverse

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


class Directory(models.Model):
	objects = None
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
	objects = None
	title = models.CharField(max_length=255)
	file = models.FileField(upload_to="users/files/%Y/%m/%d")
	directory = models.ForeignKey('Directory', on_delete=models.SET_NULL, related_name="files_set", null=True, blank=True)
	slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	file_type = models.CharField(max_length=100, null=True, blank=True)
	
	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		# print(name, extension)
		return (name, extension)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		print(self.extension()[1])
		print(self.directory)
		if self.extension()[1] in WORD:
			self.file_type = "word"
		elif self.extension()[1] in EXCEL:
			self.file_type = "excel"
		elif self.extension()[1] in POWER_POINT:
			self.file_type = "power_point"
		elif self.extension()[1] in IMAGE_TYPES:
			self.file_type = "image"
		elif self.extension()[1] in PDF:
			self.file_type = "pdf"		
		else:
			self.file_type = "undefined"			
		super(File, self).save(*args, **kwargs)

	
	def get_absolute_url(self):
		return reverse("files:file-detail", args=[self.slug])
	def __str__(self):
		return f"{self.title}{self.extension()[1]}"

