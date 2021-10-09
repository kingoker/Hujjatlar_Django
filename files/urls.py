from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("", views.DirectoryCreateListView.as_view(), name="files-list"),
	path("search/", views.search, name='search'),
	path("file/create/<uuid:uuid>/", views.FileCreateView.as_view(), name="file-create-detail"),
	path("file/create/", views.FileCreateView.as_view(), name="file-create"),
	# Shuni to'g'rila
	# path("detail/<uuid:uuid>/", views.DetailFileView.as_view(), name="file-detail"),
	path("delete/<uuid:uuid>/", views.DeleteDirectory.as_view(), name="directory-delete"),
	path("<uuid:uuid>/", views.DirectoryCreateListView.as_view(), name="files-list-detail"),

]
