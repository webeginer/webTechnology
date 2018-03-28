# -*- coding: utf-8 -*-

from django import forms

from .models import Question
from .models import Answer


# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса

class AskForm(forms.Form):
	"""docstring for AskForm"""
	title = forms.CharField(label='Заголовок', max_length=100)
	text = forms.CharField(label='Вопрос', widget=forms.Textarea)
	def __str__(self):
		return '%s %s' % (self.title, self.text)
	def clean_title(self):
		data_title = self.cleaned_data['title']
		return data_title
	def clean_text(self):
		data_text = self.cleaned_data['text']
		return data_text
	def clean(self):
		data = self.cleaned_data
		return data
	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question
	


# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом

class AnswerForm(forms.Form):
	"""docstring for AnswerForm"""
	text = forms.CharField(label='Ваш ответ', widget=forms.Textarea)
	question = forms.ModelChoiceField(queryset=Question.objects.all(), label='на вопрос №', empty_label=None)
	def __str__(self):
		return self.text
	def clean_text(self):
			data_text = self.cleaned_data['text']
			return data_text
	#def __init__(self, *args, **kwargs):
			#super(AnswerForm, self).__init__(*args, **kwargs)
			#self.fields['question'].queryset = Question.objects.filter(question__id__in=kwargs.get('id'))
	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer