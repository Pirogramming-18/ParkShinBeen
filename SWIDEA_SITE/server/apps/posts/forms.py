from django import forms
from django.forms import ModelForm
from .models import Idea

class IdeaForm(ModelForm):
	class Meta:
		model = Idea
		fields = ('title', 'image', 'content', 'interest', 'devtool')
		labels = {
			'title': '아이디어명',
			'image': '',
			'content': '아이디어 설명',
			'interest': '아이디어 관심도',
			'devtool': '예상 개발툴',		
		}