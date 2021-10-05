from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("", views.list_files, name="files-list"),
	path("search/", views.search, name='search'),
	path("<slug:slug>/", views.list_files, name="files-list-detail"),
	path("detail/<slug:slug>/", views.detail_file, name="file-detail"),
]
