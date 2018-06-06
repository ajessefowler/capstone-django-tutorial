import datetime

from django.db import models
from django.utils import timezone

'''
	Creates models for site data. This is the same as the database schema, just in Python. 
	The models inherit from models.Model. Each Question contains a question_text and pub_date, 
	as well as a __str__ method to obtain the text of the Question. The was_published_recently 
	method returns a boolean value depending on how long ago the Question was created. 
	Each Choice is joined to a Question using the models.ForeignKey() method. A Choice also 
	contains choice_text, and the number of votes cast, as well as a__str__ method to obtain
	the text of the choice.
'''

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
