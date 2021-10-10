from .models import File, Directory, Department
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs = {
			"class": "popup__input", "type": "text", "placeholder": "Название папки",
		}
		self.fields['password1'].widget.attrs = {
			"class": "popup__input", "type": "password", "placeholder": "Пароль",
		}
		self.fields['password2'].widget.attrs = {
			"class": "popup__input", "type": "password", "placeholder": "Повторите пароль",
		}

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


class CreateDirectoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateDirectoryForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {
			"class": "popup__input", "type": "text", "placeholder": "Название папки",
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
			"class": "popup__input", "name": "file", "type": "file",
		}
		self.fields['file'].label = "" 
		self.fields['file'].required = True

	class Meta:
		model = File
		fields = ("file",)

