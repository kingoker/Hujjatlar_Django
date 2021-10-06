from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("", views.list_files, name="files-list"),
	# path("file/create/", views.list_files, name="file-create"),
	path("directory/create/", views.CreateDirectoryView.as_view(), name="directory-create"),
	path("search/", views.search, name='search'),
	path("<slug:slug>/", views.list_files, name="files-list-detail"),
	path("detail/<slug:slug>/", views.DetailFileView.as_view(), name="file-detail"),
]
