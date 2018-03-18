# -*- coding: utf-8 -*-
# from __future__ import unicode_literals



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"


# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа


class QuestionManager(models.Manager):
		"""new - метод возвращающий
		 последние добавленные вопросы
		 popular - метод возвращающий
		 вопросы отсортированные по
		 рейтингу"""
		def new(self):
			return self.order_by('-added_at')
		def popular(self):
			return self.order_by('rating')		


class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	added_at = models.DateTimeField('date published')
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(
		User,
		related_name='question_author',
		)
	likes = models.ManyToManyField(
		User,
		related_name='question_likes',
		blank=True,
	)
	objects = QuestionManager()


class Answer(models.Model): 
	text = models.TextField()
	added_at = models.DateTimeField('date answer')
	question = models.ForeignKey(
		Question,
		related_name='answer_question',
	)
	author = models.ManyToManyField(
		User,
		related_name='answer_author',
		)
	def __str__(self):
		return self.text