from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("registration/", views.registration, name="registration"),
	path("", views.DirectoryCreateListView.as_view(), name="files-list"),
	path("search/", views.search, name='search'),
	path("delete/files/<uuid:uuid>/", views.DeleteFile.as_view(), name="file-delete"),
	path("delete/directories/<uuid:uuid>/", views.DeleteDirectory.as_view(), name="directory-delete"),
	path("<uuid:uuid>/", views.DirectoryCreateListView.as_view(), name="files-list-detail"),
]
