from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import File, Directory, Department
from django.views import generic
from .forms import CreateDirectoryForm


def list_files(request, slug=None):
	if slug:
		directory = get_object_or_404(Directory, slug=slug)
		directory_objects = directory.directories_of_this.all()
		file_objects = directory.files_set.all()
	else:	
		directory_objects = Directory.objects.filter(directories=None)
		file_objects = File.objects.filter(directory=None)
	directory_create_form = CreateDirectoryForm() 	
	# print(directory_objects)
	return render(request, "file/index.html", {"directory_form" : directory_create_form  , "directory_objects": directory_objects, "file_objects": file_objects, "slug": slug})


class DetailFileView(generic.DetailView):
	template_name = "file/detail.html"
	queryset = File.objects.all()
	
class CreateDirectoryView(generic.FormView):
	template_name = "file/index.html"
	form_class = CreateDirectoryForm
	success_url = '/'
# def directory_create_form(request, slug=False)


# Search form
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		directory_list = Directory.objects.filter(title__icontains=searched)
		file_list = File.objects.filter(title__icontains=searched)
		return render(request, 'file/search.html', {'searched': searched, 'directory_list': directory_list, 'file_list': file_list})
	else:
		return render(request, 'file/search.html', {})

