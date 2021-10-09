from .models import File, Directory, Department
from django import forms



class CreateDirectoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateDirectoryForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {
			"class" : "popup__input", "type" : "text", "placeholder" : "Название папки",
		}
		self.fields['title'].required = True
		self.fields['title'].label = "" 
	class Meta:
		model = Directory
		fields = ("title", )


class CreateFileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateFileForm, self).__init__(*args, **kwargs)
		self.fields['file'].widget.attrs = {
			"class" : "popup__input", "name" : "file" , "type" : "file", 
		}
		self.fields['file'].label = "" 
		self.fields['file'].required = True

	class Meta:
		model = File
		fields = ("file",)
