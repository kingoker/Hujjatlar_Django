from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("", views.CreateDirectoryView.as_view(), name="files-list"),
	# path("file/create/", views.list_files, name="file-create"),
	path("directory/create/", views.CreateDirectoryView.as_view(), name="directory-create"),
	path("search/", views.search, name='search'),
	# path("<uuid:uuid_id>/", views.testview, name="test"),
	path("detail/<uuid:uuid>/", views.DetailFileView.as_view(), name="file-detail"),
	path("<uuid:uuid>/", views.CreateDirectoryView.as_view(), name="files-list-detail"),

]
