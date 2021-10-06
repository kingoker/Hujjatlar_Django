from .models import File, Directory, Department
from django import forms

class CreateDirectoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateDirectoryForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {
			"class" : "popup__input", "type" : "text", "placeholder" : "Название папки",
		}
		self.fields['title'].label = "" 
	class Meta:
		model = Directory
		fields = ("title", )


class CreateFileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ("file", "title")
