from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from .models import File, Directory
from django.views import generic
from .forms import CreateDirectoryForm, CreateFileForm, UserRegisterForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
import logging
from django.contrib import messages
from django.views.generic import ListView


logger = logging.getLogger(__name__)


class BaseDeleteView(generic.DeleteView):
	template_name = "file/delete_directory.html"
	queryset = Directory.objects.all()
	success_url = '/'
	model = None
	
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		if request.user == self.object.author:
			success_url = self.get_success_url()
			self.object.delete()
			return HttpResponseRedirect(success_url)
		else:
			return HttpResponseForbidden()

	def get_object(self):
		obj = get_object_or_404(self.model, uuid_id=self.kwargs['uuid'])
		return obj
	
	def get(self, request, uuid, *args, **kwargs):
		obj = self.get_object()
		template = self.template_name
		return render(request, template, {"obj" : obj})	
	
	# handles post requests for deleting directory 
	def post(self, request, *args, **kwargs):
		
		return self.delete(request, *args, **kwargs)

class DeleteDirectory(BaseDeleteView):
	template_name = "file/delete_directory.html"
	queryset = Directory.objects.all()
	success_url = '/'
	model = Directory

class DeleteFile(BaseDeleteView):
	template_name = "file/delete_file.html"
	queryset = File.objects.all()
	success_url = '/'
	model = File	



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
		registration_form = UserRegisterForm()
		file_create_form = CreateFileForm()
		return render(request, "file/index.html", {"directory_form": directory_create_form, "file_form": file_create_form, "directory_objects": directory_objects, "file_objects": file_objects, "directory": directory, "registration_form": registration_form})

	def post(self, request, uuid=None, *args, **kwargs):
		logger.warning("posting files or directory")
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
				logger.warning("Form is saved under %r", directory_parent.title)
				return redirect(directory_parent.get_absolute_url())
			else:	
				messages.error(request, "Something went wrong !")	
				
		elif files and not directory_parent:
			form = CreateFileForm(request.POST, files)
			if form.is_valid():
				cd = form.cleaned_data
				created_file = File.objects.create(file=cd['file'], author=author, directory=directory_parent)
				created_file.save()
				logger.warning("Form is saved under home page")

				return redirect("/")
			else:		
				messages.error(request, "Something went wrong !")	

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


# User registration
# @require_POST
def registration(request):
	if request.method == 'POST':
		registration_form = UserRegisterForm(request.POST)
		if registration_form.is_valid():
			user = registration_form.save()
			login(request, user)
			messages.success(request, 'Вы успешно зарегистрировались')
			return redirect('/')
		else:
			messages.error(request, 'Ошибка регистрации')
	else:
		registration_form = UserRegisterForm()
	return render(request, 'file/registration.html', {"registration_form": registration_form})


def user_login(request):
	if request.method == 'POST':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			user = login_form.get_user()
			login(request, user)
			return redirect('/')
	else:
		login_form = AuthenticationForm()
	return render(request, 'file/login.html', {"login_form": login_form})


def user_logout(request):
	logout(request)
	return redirect('/')


class ProfileView(ListView):
	model = File
	template_name = "file/profile.html"

