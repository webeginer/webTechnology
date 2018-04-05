# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone

from .models import Question
from .models import Answer


# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса
# author - автор вопроса

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
	def __init__(self, user, *args, **kwargs):
		if user.is_anonymous:
			self.author = User.objects.get_or_create(
				username='guest',
				defaults={
						'password':'guestpassword', 							'last_login': timezone.now(),
				}
			)[0]
		else:
			self.author = user
		super(AskForm, self).__init__(*args, **kwargs)
	def clean(self):
		data = self.cleaned_data
		return data
	def save(self):
		question = Question(**self.cleaned_data)
		question.author = self.author
		question.save()
		return question
	


# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом
# author - автор ответа

class AnswerForm(forms.Form):
	"""docstring for AnswerForm"""
	text = forms.CharField(label='Ваш ответ', widget=forms.Textarea)
	question = forms.ModelChoiceField(queryset=Question.objects.all(), label='на вопрос №', empty_label=None)
	#author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор', empty_label=None)
	def __str__(self):
		return self.text
	def clean_text(self):
			data_text = self.cleaned_data['text']
			return data_text
	def __init__(self, user, *args, **kwargs):
		if user.is_anonymous:
			self.author = User.objects.get_or_create(
				username='guest',
				defaults={
						'password':'guestpassword', 							'last_login': timezone.now(),
				}
			)[0]
		else:
			self.author = user
		super(AnswerForm, self).__init__(*args, **kwargs)
	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.author = self.author
		answer.save()
		return answer



# SignUpForm - форма регистрации
# username - имя пользователя, логин
# email - email пользователя
# password - пароль пользователя

class SignUpForm(forms.ModelForm):
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email')
	def clean_password(self):
			data_password = self.cleaned_data['password']
			return data_password
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user