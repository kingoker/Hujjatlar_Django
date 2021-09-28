from django.urls import path
from . import views

app_name = "files"

urlpatterns = [
	path("list/", views.list_files, name="files-list"),
	path("list/<slug:slug>/", views.list_files, name="files-list-detail"),
	path("detail/<slug:slug>/", views.detail_file, name="file-detail"),
]