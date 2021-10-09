from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import File, Directory, Department
from django.views import generic
from .forms import CreateDirectoryForm, CreateFileForm
from django.http import HttpResponse

class DeleteDirectory(generic.DeleteView):
	template_name = "file/delete_directory.html"
	queryset = Directory.objects.all()
	success_url = '/'
	
	def get_object(self):
		obj = get_object_or_404(Directory, uuid_id=self.kwargs['uuid'])
		return obj
	
	def get(self, request, uuid, *args, **kwargs):
		obj = self.get_object()
		template = self.template_name
		return render(request, template, {"obj" : obj})	
	
	# handles post requests for deleting directory 
	def post(self, request, *args, **kwargs):
			return self.delete(request, *args, **kwargs)

class FileCreateView(generic.View):
	def post(self, request, uuid=None, *args, **kwargs):
		print("Posted")

class DirectoryCreateListView(generic.View):
	""" This is the view for displaying list 
	of directory and file and also  for 
	creating directories for now"""
	template_name = "file/index.html"
	form_class = CreateDirectoryForm
	success_url = '/'

	def get(self, request, uuid=None, *args, **kwargs):
		directory = None	
		if uuid:
			directory = get_object_or_404(Directory, uuid_id=uuid)
			directory_objects = directory.directories_of_this.all()
			file_objects = directory.files_set.all()
		else:	
			directory_objects = Directory.objects.filter(directories=None)
			file_objects = File.objects.filter(directory=None)
		directory_create_form = CreateDirectoryForm() 
		file_create_form = CreateFileForm()	
		return render(request, "file/index.html", {"directory_form": directory_create_form, "file_form" : file_create_form , "directory_objects": directory_objects, "file_objects": file_objects, "directory" : directory})

	def post(self, request, uuid=None, *args, **kwargs):
		print(request.FILES)
		print(request.POST)
		files = request.FILES
		directory_parent = None
		if uuid:
			directory_parent = get_object_or_404(Directory, uuid_id=uuid)
		author = request.user
		if files and directory_parent:
			form = CreateFileForm(request.POST, files)
			if form.is_valid():
				cd = form.cleaned_data
				created_file = File.objects.create(file=cd['file'], author=author, directory=directory_parent)
				created_file.save()
				return redirect(directory_parent.get_absolute_url())
				print("form is valid")

		form = CreateDirectoryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if directory_parent:
				directory_child = Directory.objects.create(author=author, title=cd.get('title'), directories=directory_parent) 	
			else:
				directory_child = Directory.objects.create(author=author, title=cd.get('title')) 	

			directory_child.save()
		if directory_parent:
			return redirect(directory_parent.get_absolute_url())	
		return redirect('/')	
			
# Search form
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		directory_list = Directory.objects.filter(title__icontains=searched)
		file_list = File.objects.filter(title__icontains=searched)
		return render(request, 'file/search.html', {'searched': searched, 'directory_list': directory_list, 'file_list': file_list})
	else:
		return render(request, 'file/search.html', {})

