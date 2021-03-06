# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse


# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"

class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	added_at = models.DateTimeField(
		'date published',
		auto_now_add=True,
		)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='question_author',
		null=True,
		)
	likes = models.ManyToManyField(
		User,
		related_name='question_likes',
		blank=True,
		)
	def __str__(self):
		return '%s %s' % (self.title, self.text)
		


# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа

class Answer(models.Model): 
	text = models.TextField()
	added_at = models.DateTimeField(
		'date published',
		auto_now_add=True,
		)
	question = models.ForeignKey(
		Question,
		on_delete=models.CASCADE,
		)
	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='answer_author',
		null=True,
		)
	def __str__(self):
		return self.text