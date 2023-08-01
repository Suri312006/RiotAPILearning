from django.db import models

# Create your models here.
class Question(models.Model):
    #fields will be stored in the database
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    #idk what foreign key means
    #foreign key = each Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)