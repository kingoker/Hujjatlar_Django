from django.shortcuts import render, get_object_or_404
from .models import File, Directory

# Create your views here.


def list_files(request, slug=None):
	if slug:
		directory = get_object_or_404(Directory, slug=slug)
		directory_objects = directory.directories_of_this.all()
		file_objects = directory.files_set.all()
	else:	
		directory_objects = Directory.objects.filter(directories=None)
		file_objects = File.objects.filter(directory=None)
	print(directory_objects)
	return render(request, "file/list.html", {"directory_objects" : directory_objects, "file_objects" : file_objects, "slug" : slug})


def detail_file(request, slug):
	file = get_object_or_404(File, slug=slug)
	return render(request, "file/detail.html", {"file" : file})
	# directory = Directory.objects.filter(id=id).first()
	# print(directory)
	# directory_objects = directory.directories_of_this.all()
	# file_objects = directory.files_set.all()
	# return render(request, "file/detail.html", {"directory" : directory, "directory_objects" : directory_objects, "file_objects" : file_objects})
